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
This is an hydrological application
link: <https://www.iac.sp.gov.br/>
"""

st.sidebar.title('About')
st.sidebar.info(markdown)
logo = 'pages/Logo_IAC_d400.jpg'
st.sidebar.image(logo, width=100)

###############################################################################

st.title('Página Recarga de aquífero')
st.markdown('Gráficos e mapas sobre a recarga de aquífero')

st.divider()

mapa_recarga = 'pages/mapa_recarga.png'

st.image(mapa_recarga, width=800)


# st.divider()



# limite = gpd.read_file(r'C:\Users\swat\Documents\app_vazao\Limite_municipal_linha.geojson')

# louveira = [-23.0794, -46.9348]
# m = folium.Map(location=louveira, tiles='cartodbpositron', control_scale=True, zoom_start=13, min_zoom=11)


# # Limite municipal de Louveira
# folium.GeoJson(limite, name = 'Limites Louveira', control = False, show = True,
#                style_function = lambda x: {
#                   'color': 'dodgerblue',
#                   'weight': 3
#                }).add_to(m)

# st_mapa = st_folium(m, width=800, height=450)
