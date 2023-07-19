# Libraries 
import pandas as pd 
import numpy as np
import plotly.express as px
import folium
import streamlit as st
from haversine import haversine
from datetime import datetime 
from streamlit_folium import folium_static
import inflection

st.set_page_config(page_title = "Paises", layout =  "wide")


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
    default = ['Brazil','England','Qatar','South Africa','Canada','Australia'])

st.sidebar.markdown( """---""" )
st.sidebar.markdown( '### Powered by Comunidade DS' )


# Filtro de transito
linhas_selecionadas = df1["country_code"].isin( country_options )
df1 = df1.loc[linhas_selecionadas, :]



# =======================================
# Layout Streamlit 
# =======================================
st.header( 'Fome Zero - Países' )
with st.container():
    st.markdown("Quantidade de Cidades Registradas por País")
    cols = ["country_code","city"]
    df_aux = (df1.loc[:,cols]
              .groupby("country_code")
              .nunique()
              .sort_values(by= "city", ascending = False)
              .reset_index())
    fig = px.bar(df_aux,x = "country_code", y ="city", text_auto = True , labels ={"country_code":"Países","city":"Quantidade de Cidades"} )
    st.plotly_chart( fig, use_container_width= True)
    
with st.container():

    st.markdown("Quantidade de Restaurantes Registrados por País")
    cols = ["country_code","restaurant_id"]
    df_aux1 = (df1.loc[:,cols]
              .groupby("country_code")
              .nunique()
              .sort_values(by= "restaurant_id", ascending = False)
              .reset_index())
    fig = px.bar(df_aux1,x = "country_code", y ="restaurant_id", text_auto = True , labels ={"country_code":"Países","restaurant_id":"Quantidade de Restaurantes"} )
    st.plotly_chart( fig, use_container_width= True)
    
with st.container():
    st.markdown("Relação entre Quantidade de Restaurantes por Cidade nos Paises")
    df_city = pd.merge(df_aux,df_aux1, how = "inner")
    df_city["rest_by_city"] = df_city["restaurant_id"]/df_city["city"]
    df_city = df_city.sort_values(by= "restaurant_id", ascending = False)
    fig = px.bar(df_city,x = "country_code", y ="rest_by_city", text_auto = True ,labels ={"country_code":"Países","rest_by_city":"Relação entre Restaurantes e Cidades"})
    st.plotly_chart( fig, use_container_width= True)

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("Quantidade Média de Avaliações feitas por País")
        cols = ["country_code","votes"]
        df_aux = (df1.loc[:,cols]
                  .groupby("country_code")
                  .agg({"votes":["mean","std"]})
                  .reset_index())
        df_aux.columns = ["country","avg","std"]    
        df_aux = df_aux.sort_values(by="avg", ascending = False)
        fig = px.bar(df_aux,x = df_aux["country"], y = df_aux["avg"], text_auto = ".2f",labels ={"country":"Países","avg":"Quantidade de Avaliações Registradas"})
        st.plotly_chart( fig, use_container_width= True)     

    with col2:
        st.markdown("Nota Média por País")
        #9. Qual o nome do país que possui, na média, a maior nota média registrada?
        cols = ["country_code","aggregate_rating"]
        df_aux = (df1.loc[:,cols]
                     .groupby("country_code")
                     .agg({"aggregate_rating":["mean","std"]})
                     .reset_index())
        df_aux.columns = ["country","avg","std"]
        df_aux = df_aux.sort_values(by= "avg", ascending = False)
        
        fig = px.bar(df_aux,x = df_aux["country"], y = df_aux["avg"], text_auto = ".2f" , error_y =  df_aux["std"], labels ={"country":"Países","avg":"Nota Média"})
        st.plotly_chart( fig, use_container_width= True)  
        



