# Libraries 
import pandas as pd 
import numpy as np
import plotly.express as px
import folium
import streamlit as st
import inflection

from streamlit_folium import folium_static
from folium.plugins import MarkerCluster
from haversine import haversine
from datetime import datetime 

st.set_page_config(page_title="Home")

#----------------------
# Funções
#---------------------- 

# limpeza de Dados 
def clean_code(df1):
    df1 =df.copy()
    
    
    def rename_columns(dataframe):
        df = dataframe.copy()
        title = lambda x: inflection.titleize(x)
        snakecase = lambda x: inflection.underscore(x)
        spaces = lambda x: x.replace(" ", "")
        cols_old = list(df.columns)
        cols_old = list(map(title, cols_old))
        cols_old = list(map(spaces, cols_old))
        cols_new = list(map(snakecase, cols_old))
        df.columns = cols_new
        return df
    
    df1 = rename_columns(df1)
    
    # Criação do Tipo de Categoria de Comida
    
    def create_price_tye(price_range):
        if price_range == 1:
            return "cheap"
        elif price_range == 2:
            return "normal"
        elif price_range == 3:
            return "expensive"
        else:
            return "gourmet"
    
    for i in range(len(df1["price_range"])):
        df1.loc[i,"price_range"] = create_price_tye(df1.loc[i,"price_range"])
    
    # Preenchimento do nome dos países
    
    COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
    }
    def country_name(country_id):
        return COUNTRIES[country_id]
    
    for i in range(len(df1["country_code"])):
        df1.loc[i,"country_code"] = country_name(df1.loc[i,"country_code"])
        
    
    # Criação do nome das Cores
    
    COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
    }
    def color_name(color_code):
        return COLORS[color_code]
    
    for i in range(len(df1["rating_color"])):
        df1.loc[i,"rating_color"] = color_name(df1.loc[i,"rating_color"])
    
    
    # Remoção da coluna  "15  Switch to order menu "
    df1 =df1.drop(["switch_to_order_menu"], axis =1)
    
    # Remoção dos valores nulos 
    df1 = df1.dropna()
    
    # Caracterizar restaurantes pelo primeiro tipo de comida
    df1["cuisines"] = df1.loc[:, "cuisines"].apply(lambda x: x.split(",")[0])
    
    # Remoção dos dados duplicados
    df1 = df1.drop_duplicates(keep = "first")
    
    # Atualizando o Index
    df1 = df1.reset_index(drop = True)
    
    return df1

#--------------------------------------------------------------------------------------------------------------------------------

# Import Dataset
df = pd.read_csv("zomato.csv")

# limpeza de Dados 

df1 = clean_code(df)    



# =======================================
# Barra Lateral
# =======================================
st.sidebar.markdown( '# Fome Zero' )
st.sidebar.markdown( '## Marketplace de Restaurantes' )
st.sidebar.markdown( """---""" )

st.sidebar.markdown( """---""" )

st.sidebar.markdown( '# Filtros' )
country_options = st.sidebar.multiselect(
    'Defina os Países qe deseja visualizar as informações',
    ['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'],
    default = ['Philippines', 'Brazil', 'Australia', 'United States of America',
       'Canada', 'Singapure', 'United Arab Emirates', 'India',
       'Indonesia', 'New Zeland', 'England', 'Qatar', 'South Africa',
       'Sri Lanka', 'Turkey'])

st.sidebar.markdown( """---""" )
st.sidebar.markdown( '### Powered by Comunidade DS' )


# Filtro de transito
linhas_selecionadas = df1["country_code"].isin( country_options )
df1 = df1.loc[linhas_selecionadas, :]



# =======================================
# Layout Streamlit 
# =======================================


st.write("# Fome Zero")

with st.container():
    st.markdown("## Principais Indicadores")
    col1, col2, col3, col4, col5  = st.columns( 5 )
    with col1:
        rest_unique = df1.loc[:,"restaurant_id"].nunique()
        col1.metric("Restaurantes",rest_unique)
            
    with col2:    
        country_unique = df1.loc[:,"country_code"].nunique()
        col2.metric("Países",country_unique )
        
    with col3:    
        city_unique = df1.loc[:,"city"].nunique()
        col3.metric("Cidades",city_unique )
        
    with col4:    
        sum_rating = df1.loc[:,"votes"].sum()
        col4.metric("Total de Avaliações",sum_rating)
        
    with col5:    
        cuisines_unique = df1.loc[:,"cuisines"].nunique()
        col5.metric("Culinárias",cuisines_unique)

   
    
with st.container():
    columns = ['restaurant_name', 'aggregate_rating', 'longitude', 'latitude']
    columns_groupby = ['restaurant_name', 'aggregate_rating']
    
    data_plot = df1.loc[:, columns].groupby( columns_groupby ).mean().reset_index()
    
    # Desenhar o mapa
    map = folium.Map( [24.21,81.08] ,zoom_start=1 )
    mCluster = MarkerCluster(name = "Markers Demo").add_to(map)
    for index, location_info in data_plot.iterrows():
       folium.Marker( [location_info['latitude'],
                      location_info['longitude']], 
                      popup=location_info[['restaurant_name', 'aggregate_rating']] ).add_to( mCluster)

    folium_static(map, width =800, height = 600  )
    
with st.container():
    st.markdown (
        """
        Fome Zero Dashboard foi construído para acompanhar as métricas de crescimento do Marketplace de Restaurantes.
        ### Ask for Help
        - Lucas de Paula
    """)
    