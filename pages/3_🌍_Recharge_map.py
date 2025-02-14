import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium

#Configurando a página do app streamlit
st.set_page_config(
    page_title='Hydro App',
    layout='wide',
    initial_sidebar_state='expanded'
)

markdown = """
Esta página exibe mapas de recarga de aquífero
"""

st.sidebar.title('Sobre')
st.sidebar.info(markdown)
logo = 'pages/Logo_IAC_d400.jpg'
st.sidebar.image(logo, width=100)

###############################################################################

#Criando a sidebar
sidebar = st.sidebar.empty()

list_watersheds = ['Atibaia cabeceira', 'Camanducaia', 'Capivari', 'Corumbataí', 'Jundiaí']

#Selectbox de seleção da bacia
st.sidebar.header('Escolha uma bacia')
watershed_select = st.sidebar.selectbox('Selecione', list_watersheds)

#Mapas das bacias
mapa_rec_atibaia_cab = 'pages/recharge_maps/rch_map_atibaia_cabeceira.png'
mapa_rec_camanducaia = 'pages/recharge_maps/rch_map_camanducaia.png'
mapa_rec_capivari = 'pages/recharge_maps/rch_map_capivari.png'
mapa_rec_corumbatai = 'pages/recharge_maps/rch_map_corumbatai.png'
mapa_rec_jundiai = 'pages/recharge_maps/rch_map_jundiai.png'

if watershed_select == 'Atibaia cabeceira':
    recharge_map = mapa_rec_atibaia_cab
elif watershed_select == 'Camanducaia':
    recharge_map = mapa_rec_camanducaia
elif watershed_select == 'Capivari':
    recharge_map = mapa_rec_capivari
elif watershed_select == 'Corumbataí':
    recharge_map = mapa_rec_corumbatai
else:
    recharge_map = mapa_rec_jundiai


st.title('Recarga de aquíferos das sub-bacias PCJ')
st.markdown('Mapas de recarga de aquíferos das sub-bacias PCJ')

st.divider()

st.subheader(f'Bacia: {watershed_select}')
st.image(recharge_map, width=900)


# st.divider()