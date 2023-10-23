import streamlit as st
import pandas as pd 

st.set_page_config(
    'mimosa'
    'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.minijogos.com.br%2Fjogo%2Ffive-nights-at-freddys&psig=AOvVaw1UeNSktWEU-DvXY-8u2I1J&ust=1698155739600000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCOib5qGpjIIDFQAAAAAdAAAAABAD'

)

st.title('PAGINA DE TESTE')

esportes = pd.read_csv(
    'https://github.com/MainakRepositor/Datasets/raw/master/GeneralEsportData.csv',
     enconding= 'latin-1')
st.dataframe(esportes)