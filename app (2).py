import streamlit as st
import pandas as pd
import plotly.express as px

# Configura la pàgina
st.set_page_config(page_title="Anàlisi de Clients per Franja Horària", layout="centered")

# Títol de l'aplicació
st.title("📊 Anàlisi de Clients per Franja Horària")

# Carrega les dades
@st.cache_data
def carregar_dades():
    return pd.read_csv("dades_clients.csv")

df = carregar_dades()

# Mostra les dades (opcional)
with st.expander("📂 Mostra les dades crues"):
    st.dataframe(df)

# Filtra per dia si està disponible
dies_disponibles = df["Dia"].unique()
dia_seleccionat = st.selectbox("🗓️ Selecciona un dia:", dies_disponibles)

df_filtrat = df[df["Dia"] == dia_seleccionat]

# Gràfic de barres
fig = px.bar(
    df_filtrat,
    x="Franja Horària",
    y="Nombre de Clients",
    title=f"Nombre de clients per franja horària - {dia_seleccionat}",
    labels={"Franja Horària": "Franja Horària", "Nombre de Clients": "Nombre de Clients"},
    color_discrete_sequence=["#636EFA"]
)

st.plotly_chart(fig, use_container_width=True)

# Estadístiques bàsiques
st.subheader("📈 Estadístiques bàsiques")
col1, col2 = st.columns(2)
col1.metric("Total de clients", int(df_filtrat["Nombre de Clients"].sum()))
col2.metric("Franja amb més afluència", df_filtrat.loc[df_filtrat["Nombre de Clients"].idxmax(), "Franja Horària"])
