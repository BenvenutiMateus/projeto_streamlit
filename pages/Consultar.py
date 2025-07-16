import streamlit as st
import pandas as pd

# --- Configuração da Página ---
st.set_page_config(
    page_title="Consulta de Clientes",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 Consulta de Clientes")
st.divider()

# --- Lógica para ler e exibir os clientes ---
try:
    # Tenta ler o arquivo CSV. Adicionamos nomes para as colunas.
    df_clientes = pd.read_csv("clientes.csv", header=None, names=["Nome", "Data de Nascimento", "Tipo"])
    st.write("Abaixo está a lista de clientes cadastrados:")
    st.dataframe(df_clientes, use_container_width=True)

except FileNotFoundError:
    # Se o arquivo não for encontrado, mostra um aviso amigável.
    st.warning("Nenhum cliente cadastrado ainda. Cadastre um cliente na página principal para vê-lo aqui.")

except Exception as e:
    # Se ocorrer qualquer outro erro, informa o usuário.
    st.error(f"Ocorreu um erro inesperado ao tentar ler os dados: {e}")