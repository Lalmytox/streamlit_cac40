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

show_ma20 = st.sidebar.checkbox("Moyenne mobile 20j", True)
show_ma50 = st.sidebar.checkbox("Moyenne mobile 50j", False)
show_ma200 = st.sidebar.checkbox("Moyenne mobile 200j", False)

# ----------------------------
# FILTER DATA
# ----------------------------
mask = (df["Date"] >= pd.to_datetime(start_date)) & (df["Date"] <= pd.to_datetime(end_date))
df_filtered = df.loc[mask]

# ----------------------------
# KPIs
# ----------------------------

# ----------------------------
# KPIs SUR LA PERIODE
# ----------------------------

st.subheader("Dernière scéance")

last_row = df_filtered.iloc[-1]
prev_row = df_filtered.iloc[-2]


col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "💰 Cours de clôture",
    f"{last_row['Close']:.2f} €",
    f"{last_row['Close'] - prev_row['Close']:.2f} €"
)

col2.metric(
    "📦 Volume",
    f"{int(last_row['Number of Shares']):,}".replace(",", " ")
)

col3.metric(
    "🔄 Transactions",
    int(last_row["Number of Trades"])
)

col4.metric(
    "⚖️ VWAP",
    f"{last_row['vwap']:.2f} €"
)


st.markdown("---")
st.subheader("Historique")

start_price = df_filtered.iloc[0]["Close"]
end_price = df_filtered.iloc[-1]["Close"]

# Performance (%)
performance = (end_price - start_price) / start_price * 100

# Volatilité (%)
returns = df_filtered["Close"].pct_change().dropna()
volatility = returns.std() * 100

# Volume moyen
avg_volume = df_filtered["Number of Shares"].mean()

# VWAP moyen pondéré
vwap_period = (
    (df_filtered["vwap"] * df_filtered["Number of Shares"]).sum()
    / df_filtered["Number of Shares"].sum()
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "📈 Performance période",
    f"{performance:.2f} %",
) # Mesure le gain ou la perte sur la période

col2.metric(
    "📊 Volatilité",
    f"{volatility:.2f} %",
) # Mesure le risque / l’instabilité du titre

col3.metric(
    "📦 Volume moyen",
    f"{int(avg_volume):,}".replace(",", " ")
) # Indique la liquidité moyenne sur la période

col4.metric(
    "⚖️ VWAP période",
    f"{vwap_period:.2f} €"
) # Représente le prix moyen réellement payé sur toute la période




# ----------------------------
# CANDLESTICK CHART
# ----------------------------
fig = go.Figure()

fig.add_trace(go.Candlestick(
    x=df_filtered["Date"],
    open=df_filtered["Open"],
    high=df_filtered["High"],
    low=df_filtered["Low"],
    close=df_filtered["Close"],
    name="Cours"
))

if show_ma20:
    fig.add_trace(go.Scatter(
        x=df_filtered["Date"],
        y=df_filtered["Close"].rolling(20).mean(),
        name="MA 20"
    ))

if show_ma50:
    fig.add_trace(go.Scatter(
        x=df_filtered["Date"],
        y=df_filtered["Close"].rolling(50).mean(),
        name="MA 50"
    ))

if show_ma200:
    fig.add_trace(go.Scatter(
        x=df_filtered["Date"],
        y=df_filtered["Close"].rolling(200).mean(),
        name="MA 200"
    ))

fig.update_layout(
    title="📈 Cours de l'action",
    xaxis_title="Date",
    yaxis_title="Prix (€)",
    height=600
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ----------------------------
# VOLUME CHART
# ----------------------------
st.subheader("📉 Volumes échangés")

fig_volume = go.Figure()
fig_volume.add_trace(go.Bar(
    x=df_filtered["Date"],
    y=df_filtered["Number of Shares"],
    name="Volume"
))

fig_volume.update_layout(
    height=300,
    xaxis_title="Date",
    yaxis_title="Volume"
)

st.plotly_chart(fig_volume, use_container_width=True)