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

st.set_page_config(page_title = "Culinaria", layout =  "wide")


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
    
# Tipos de Culinaria 
def cousine (df1,culinaria):
    cols = ["country_code","city","restaurant_name","aggregate_rating","restaurant_id"]
    linhas = (df1["cuisines"] == culinaria) 
    df_aux = (df1.loc[linhas,cols]
              .groupby(["restaurant_id","restaurant_name","city","country_code"])
              .agg({"aggregate_rating":"mean"})
              .sort_values(by= "aggregate_rating", ascending = False)
              .reset_index())
    
    linhas = df_aux["aggregate_rating"]==df_aux["aggregate_rating"].max()
    df_aux = (df_aux.loc[linhas,:]
                    .sort_values( by = "restaurant_id",  ascending = True))
    return df_aux

# Top Culinarias 
def types_cousine(df1, ordem ):
    cols = ["cuisines","aggregate_rating"]
    df_aux = (df1.loc[:,cols]
              .groupby(["cuisines"])
              .agg({"aggregate_rating":"mean"})
              .sort_values(by= "aggregate_rating", ascending = ordem)
              .reset_index())
    fig = px.bar(df_aux.head(10),x = "cuisines", y ="aggregate_rating", text_auto = True ,labels ={"aggregate_rating":"Média das avaliações","cuisines":"Tipos de Culinária"})
    return fig



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
st.header( 'Fome Zero - Tipos de Culinárias' )

with st.container():
    st.markdown("## Melhores Restaurantes dos Principais Tipos Culinários")
    col1, col2, col3, col4, col5  = st.columns( 5, gap='large' )
    
    with col1:
        df_cousine = cousine(df1,"Italian")       
        col1.metric(df_cousine.iloc[0,1],df_cousine.iloc[0,4], "Italian")


    with col2:    
        df_cousine = cousine(df1,"American")       
        col2.metric(df_cousine.iloc[0,1],df_cousine.iloc[0,4], "American")

    with col3:    
        df_cousine = cousine(df1,"Arabian")       
        col3.metric(df_cousine.iloc[0,1],df_cousine.iloc[0,4], "Arabian")

    with col4:    
        df_cousine = cousine(df1,"Japanese")       
        col4.metric(df_cousine.iloc[0,1],df_cousine.iloc[0,4], "Japanese")

    with col5:    
        df_cousine = cousine(df1,"Brazilian")       
        col5.metric(df_cousine.iloc[0,1],df_cousine.iloc[0,4], "Brazilian")

        

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("Top 10 Melhores Tipos de Culinárias")
        fig = types_cousine(df1,False)    
        st.plotly_chart( fig, use_container_width= True)  
         
    with col2:
        st.markdown("Top 10 Piores Tipos de Culinárias")
        fig = types_cousine(df1,True)    
        st.plotly_chart( fig, use_container_width= True)  
    

            




