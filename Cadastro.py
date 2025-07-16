import streamlit as st
import pandas as pd
from datetime import date

def gravar_dados(nome, data_nasc, tipo):
    if not nome or data_nasc >= date.today() or not tipo:
        st.session_state["sucesso"] = False
        return
    st.session_state["sucesso"] = True
    # Aqui você pode adicionar a lógica para gravar os dados em um banco de dados ou arquivo
    with open("clientes.csv", "a") as f:
        f.write(f"{nome},{data_nasc},{tipo}\n")

st.set_page_config(
    page_title="Cadastro de clientes", 
    page_icon=":guardsman:", layout="wide"
    )

st.title("Cadastro de clientes")
st.divider()

nome = st.text_input("Digite o nome do cliente",
                    key="nome_cliente")

dt_nasc = st.date_input("Data nascimento",
                        format="DD/MM/YYYY")

tipo = st.selectbox("Tipo do cliente",
                    ["Pessoa Jurídica","Pessoa Física"],
                    placeholder="Selecione o tipo"
                    )

btn_cadastrar = st.button("Cadastrar", on_click=gravar_dados,
                        args=(nome, dt_nasc, tipo))

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso",
                icon="✅")
    else:
        st.error("Preencha os dados corretamente",
                icon="❌")