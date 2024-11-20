import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

with st.sidebar:
    st.page_link("app.py", label="App")
    st.page_link("pages/lista_de_escolas.py", label="Lista de Escolas")
    st.page_link("pages/alunos_escola.py", label="Métricas por Escolas")
    st.page_link("pages/ordenar_escolas_por_qt_alunos.py", label="Escolas por Quantidade de Alunos")
    st.page_link("pages/crud_usuario.py", label="Cadastrar Usuário")
    st.page_link("pages/turma_por_escola.py", label="Turmas por escola")

st.header("**Home**")