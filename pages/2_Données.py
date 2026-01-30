import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ----------------------------
# CONFIG
# ----------------------------
st.set_page_config(
    page_title="Suivi boursier - Fnac Darty",
    layout="wide"
)

# =========================
# Titre et logo
# =========================

col1, col2 = st.columns([1, 3])  # ajuster les ratios

with col1:
    st.image("fnac_darty.png", width=200)

st.title("📊 Outil de suivi boursier – Fnac Darty")

# ----------------------------
# LOAD DATA
# ----------------------------
@st.cache_data
def load_data():
    df = pd.read_csv(
        "fnac_darty.csv",
        sep=";",
        dayfirst=True,
        parse_dates=["Date"]
    )
    df = df.sort_values("Date")
    return df

df = load_data()

# ----------------------------
# SIDEBAR
# ----------------------------
st.sidebar.header("⚙️ Paramètres")

start_date = st.sidebar.date_input(
    "Date de début",
    df["Date"].min()
)

end_date = st.sidebar.date_input(
    "Date de fin",
    df["Date"].max()
)

# ----------------------------
# FILTER DATA
# ----------------------------
mask = (df["Date"] >= pd.to_datetime(start_date)) & (df["Date"] <= pd.to_datetime(end_date))
df_filtered = df.loc[mask]

# ----------------------------
# DATA TABLE
# ----------------------------
st.subheader("🧾 Données brutes")
st.dataframe(df_filtered)
st.download_button(
    label="📥 Télécharger les données filtrées (CSV)",
    data=df_filtered.to_csv(index=False).encode('utf-8'),
    file_name='fnac_darty_filtered.csv',
    mime='text/csv'
)