import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium
import branca

st.set_page_config(
    page_title='Hydro App',
    layout='wide',
    initial_sidebar_state='expanded'
)

#Texto na sidebar de apresentação do app
markdown = """
Esta aplicação exibe dados da tese desenvolvida no PPG-IAC.

IAC: <https://www.iac.sp.gov.br/>\n
PG-IAC: <https://www.iac.sp.gov.br/areadoinstituto/posgraduacao/>
"""

st.sidebar.title('Sobre')
st.sidebar.info(markdown)
logo = 'Logo_IAC_d400.jpg'
st.sidebar.image(logo, width=100)

###############################################################################

col1, col2 = st.columns([0.3, 0.7])

with col1:
    st.title('App Hidro')
    st.markdown(
        """
        Este aplicativo foi desenvolvido para divulgar parte dos resultados obtidos da tese desenvolvida no PPG-IAC.\n
        Instituto Agronômico de Campinas (IAC) <https://www.iac.sp.gov.br/>
        """
    )

###############################################################################

col2.header('Sub-bacias :blue[PCJ]')

subs_pcj = gpd.read_file('subs_pcj.geojson')                # Camada original --> C:\Users\swat\Documents\app_vazao\subs_pcj.geojson
drenagem = gpd.read_file('rede_drenagem.geojson')           # Camada de drenagem também está simplificada


centro = [-22.7956, -47.2072]
min_lat, max_lat = -22.0067, -23.3637
min_lon, max_lon = -45.7889, -48.5410

m = folium.Map(location=centro, tiles=None, control_scale=False, zoom_start=9, scrollWheelZoom=False,
               dragging=False, zoom_control=False, max_bounds=True, min_lat=min_lat, max_lat=max_lat, min_lon=min_lon, max_lon=max_lon)

#m.add_child(folium.LatLngPopup())

#Adicionando Marcadores de círculo para visualizar os limites do mapa
# folium.CircleMarker([max_lat, min_lon], color='navy', tooltip="Lower Right Corner").add_to(m)
# folium.CircleMarker([min_lat, min_lon], color='navy', tooltip="Upper Right Corner").add_to(m)
# folium.CircleMarker([min_lat, max_lon], color='navy', tooltip="Upper Left Corner").add_to(m)
# folium.CircleMarker([max_lat, max_lon], color='navy', tooltip="Lower Left Corner").add_to(m)


#Tiles
white_BG = folium.TileLayer(tiles=branca.utilities.image_to_url([[1,1], [1,1]]), attr='W', name='White mode', overlay=False, control=True).add_to(m)
# folium.TileLayer('cartodbpositron', name='Light mode', overlay=False, control=True).add_to(m)


# Mapa das sub-bacias da PCJ

#Função de destaque
def highlight_function(feature):
    return {
          'fillColor': '#87d4af',
          'fillOpacity': 1.0,
          'color': '#87d4af',
          'weight': 1.0
           }

#Sub-bacias PCJ
folium.GeoJson(subs_pcj, name='PCJ subbasins', control=True, show=True, zoom_on_click=False,
               tooltip = folium.GeoJsonTooltip(fields = ['SUBS'],
                                               aliases = ['SUB-BACIA:'],
                                               sticky = True,
                                               labels=True,
                                               style = """
                                               background-color: #F0EFEF;
                                               border: 2px solid black;
                                               border-radius: 3px;
                                               box-shadow: 3px;
                                               """),
               style_function = lambda x: {
                   'fillColor': '#e6e6e6',
                   'fillOpacity': 1.0,
                   'color': 'black',
                   'weight': 1.0},
               highlight_function=highlight_function
               ).add_to(m)


#Rede de drenagem
folium.GeoJson(drenagem, name='Drenagem', control=True, show=True, zoom_on_click=False,
               style_function = lambda x: {
                   'color': 'deepskyblue',
                   'weight': 1}
                   ).add_to(m)


#Adicionar painel de controle de camadas
# folium.LayerControl(collapsed=False).add_to(m)

#Manter o fundo branco em frente ao tile cartodbpositron
m.keep_in_front(white_BG)

with col2:
    st_mapa = st_folium(m, width=1000, height=600, use_container_width=True, returned_objects=[])    # Ver sobre "returned_objects" em https://folium.streamlit.app/static_map


#CRS da camada
# crs = subs_pcj.crs
# st.write(crs)
