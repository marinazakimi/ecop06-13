import streamlit as st
import pandas as pd 

st.set_page_config(
    'mimosa'
    'https://unifei.edu.br/wp-content/themes/twentytwelve-child/img/cabecalho/logo-unifei-oficial.png'

)

st.title('PAGINA DE TESTE')

esportes = pd.read_csv(
    'https://github.com/MainakRepositor/Datasets/raw/master/GeneralEsportData.csv',
     encoding= 'latin-1')

    
st.dataframe(esportes)