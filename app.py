import streamlit as st
import pandas as pd
import plotly.express as px
import json

# Função para carregar os dados do JSON
def load_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return pd.DataFrame(data)

# Carregar os dados
df = load_data()

# Mostrar uma imagem
st.image("./myPhoto.png", caption="edwDev", use_column_width=False, width=100)

# Titulo da aplicação
st.title("Gráfico de Pizza com Dados Aleatórios")

# Mostrar os dados em uma tabela
st.write("Dados carregados: ")
st.write(df)

# Criar o gráfico de pizza
fig = px.pie(df, names='category', values='values', title='Distribuição dos Valores por Categoria')

# Mostrar o gráfico
st.plotly_chart(fig)

# Informação sobre os dados
st.write("Os dados foram gerado aleatóriamente e carregados de um arquivo JSON.")