import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
import numpy as np

st.set_page_config(page_title="Fnac Darty – Analyse boursière", layout="wide")

# =========================
# Thème CSS personnalisé
#ffffff; /* blanc */
#ffcc00; /* jaune Fnac */
# =========================
st.markdown(
    """
    <style>
    /* Conteneur principal (vue) */
    [data-testid="stAppViewContainer"] {
        background-color: #ffffff; /* blanc */
        color: #000000;            /* texte noir */
    }

    /* Barre latérale */
    [data-testid="stSidebar"] {
        background-color: #e0e0e0; /* gris */
    }

    /* Titres (st.title, st.header, st.subheader) */
    h1, h2, h3 {
        color: #ff0000; /* rouge Fnac */
    }

    /* Boutons */
    .stButton > button {
        background-color: #ff0000;
        color: #ffffff;
        border-radius: 8px;
        border: none;
    }
    .stButton > button:hover {
        background-color: #cc0000;
        color: #ffffff;
    }

    /* Optionnel : cartes/containers */
    .stContainer, .stMarkdown, .stDataFrame {
        color: inherit;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("""
<style>
[data-baseweb="option"] {
    background-color: #ffcc00 !important;  /* jaune Fnac */
    color: #000000 !important;
}
[data-baseweb="option"]:hover {
    background-color: #ff0000 !important;  /* rouge Fnac */
    color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

# =========================
# Titre et logo
# =========================
col1, col2 = st.columns([1, 3])  # ajuster les ratios

with col1:
    st.image("fnac_darty.png", width=200)

with col2:
    st.title("Fnac Darty - Analyse boursière (12DM)")


# st.title("📈 Fnac Darty – Analyse boursière (12 derniers mois)")
# st.markdown("Application Streamlit pour analyser les données boursières de Fnac Darty.")

# =========================
# Chargement des données
# =========================
@st.cache_data
def load_data():
    df = pd.read_csv("fnac_darty.csv", sep=";")
    df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
    df = df.sort_values("Date")
    return df

try:
    df = load_data()
except Exception:
    st.error("Impossible de charger le fichier 'fnac_darty.csv'")
    st.stop()

# =========================
# Sidebar
# =========================

# Menu sidebar
with st.sidebar:
    selected = option_menu(
        menu_title="Navigation",  # titre du menu
        options=["Résumé", "Graphiques", "Données brutes"],
        icons=["house", "bar-chart", "table"],  # icônes
        menu_icon="cast",  # icône du menu
        default_index=0     )



# --- Sidebar : filtres communs ---
st.sidebar.header("⚙️ Paramètres")

start_date = st.sidebar.date_input("Date de début", df["Date"].min())
end_date = st.sidebar.date_input("Date de fin", df["Date"].max())

mask = (df["Date"] >= pd.to_datetime(start_date)) & (df["Date"] <= pd.to_datetime(end_date))
df_filtered = df.loc[mask]


# ------------------------
# Contenu
# ------------------------


if selected == "Résumé":
    st.subheader("📊 Indicateurs clés")

    # --- Calcul des KPIs ---
    dernier_cours = df_filtered['Close'].iloc[-1]
    premier_cours = df_filtered['Close'].iloc[0]
    plus_haut = df_filtered['High'].max()
    plus_bas = df_filtered['Low'].min()
    variation = (dernier_cours - premier_cours) / premier_cours * 100
    close_moyen = df_filtered['Close'].mean()
    vwap_moyen = df_filtered['vwap'].mean()

    volume_total = df_filtered['Number of Shares'].sum()
    nb_trades_total = df_filtered['Number of Trades'].sum()
    turnover_total = df_filtered['Turnover'].sum()
    volume_moyen = df_filtered['Number of Shares'].mean()

    # Volatilité / risque
    rendements_journaliers = df_filtered['Close'].pct_change()
    volatilite_journaliere = rendements_journaliers.std()
    volatilite_annualisee = volatilite_journaliere * np.sqrt(252)
    max_drawdown = (df_filtered['Close']/df_filtered['Close'].cummax() - 1).min() * 100

    # =========================
    # Bloc 1 : Performance / Cours
    # =========================
    st.subheader("📈 Performance / Cours")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Dernier cours", f"{dernier_cours:.2f} €")
    col2.metric("Plus haut", f"{plus_haut:.2f} €")
    col3.metric("Plus bas", f"{plus_bas:.2f} €")
    col4.metric("Variation sur période", f"{variation:.2f} %")

    # Ligne supplémentaire si besoin
    col1, col2, col3 = st.columns(3)
    col1.metric("Cours moyen", f"{close_moyen:.2f} €")
    col2.metric("VWAP moyen", f"{vwap_moyen:.2f} €")
    col3.metric("Premier cours", f"{premier_cours:.2f} €")

    # =========================
    # Bloc 2 : Volume et liquidité
    # =========================
    st.subheader("📦 Volume et liquidité")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Volume total", f"{volume_total:,}")
    col2.metric("Volume moyen/jour", f"{volume_moyen:,.0f}")
    col3.metric("Nb de trades total", f"{nb_trades_total:,}")
    col4.metric("Turnover total (€)", f"{turnover_total:,.0f}")

    # =========================
    # Bloc 3 : Volatilité / Risque
    # =========================
    st.subheader("⚠️ Volatilité / Risque")
    col1, col2, col3 = st.columns(3)
    col1.metric("Volatilité journalière", f"{volatilite_journaliere:.2%}")
    col2.metric("Volatilité annualisée", f"{volatilite_annualisee:.2%}")
    col3.metric("Max Drawdown", f"{max_drawdown:.2f} %")




elif selected == "Graphiques":
    st.subheader("💹 Évolution du cours")
    fig_price = px.line(df_filtered, x="Date", y="Close", color_discrete_sequence=['#ff0000'])
    st.plotly_chart(fig_price, use_container_width=True)
    
    st.subheader("📦 Volume échangé")
    fig_volume = px.bar(df_filtered, x="Date", y="Number of Shares", color_discrete_sequence=['#ffcc00'])
    st.plotly_chart(fig_volume, use_container_width=True)
    
    st.subheader("📐 Cours vs VWAP")
    fig_vwap = px.line(df_filtered, x="Date", y=["Close", "vwap"],
                       labels={"value":"Prix (€)", "variable":"Indicateur"},
                       color_discrete_sequence=['#ff0000','#000000'])
    st.plotly_chart(fig_vwap, use_container_width=True)


elif selected == "Données brutes":
    st.subheader("📋 Données brutes")
    st.dataframe(df_filtered, use_container_width=True)
    st.download_button(
        label="📥 Télécharger les données filtrées (CSV)",
        data=df_filtered.to_csv(index=False),
        file_name="fnac_darty_filtre.csv",
        mime="text/csv"
    )

