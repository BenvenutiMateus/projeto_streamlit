import streamlit as st
import pandas as pd

st.title("Consultar Clientes")
st.divider()

@st.cache_data
def carregar_dados():

    df = pd.read_csv("clientes.csv")
    return df


df_clientes = carregar_dados()
if not df_clientes.empty:
    st.dataframe(df_clientes, hide_index=True)
