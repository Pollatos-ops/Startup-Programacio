
import streamlit as st
import pandas as pd
import math

# Carreguem el CSV amb les dades
df = pd.read_csv("dades_clients.csv")

st.title("Gestió de Caixes per Franja Horària")
st.write("Aquest programa analitza les dades de clients per hora i recomana si cal obrir més caixes.")

# Mostrem les hores disponibles
hores_disponibles = df['hora'].unique()
hora_usuari = st.selectbox("Selecciona una hora per analitzar:", hores_disponibles)

# Filtratge per hora escollida
fila = df[df['hora'] == hora_usuari]

if not fila.empty:
    clients = int(fila.iloc[0]['clients'])
    max_clients_per_caixa = 10
    max_caixes = 6

    caixes_necessaries = min(math.ceil(clients / max_clients_per_caixa), max_caixes)
    clients_per_caixa = clients / caixes_necessaries

    st.write(f"**Nombre de clients a les {hora_usuari}h:** {clients}")
    st.write(f"**Caixes recomanades a obrir:** {caixes_necessaries}")
    st.write(f"**Clients per caixa:** {clients_per_caixa:.2f}")

    if caixes_necessaries == max_caixes and clients_per_caixa > max_clients_per_caixa:
        st.warning("Totes les caixes estan obertes i encara hi ha massa clients per caixa.")
    else:
        st.success("Flux correcte. No cal obrir més caixes.")
else:
    st.error("No s’han trobat dades per aquesta hora.")
