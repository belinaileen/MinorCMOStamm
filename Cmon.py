from cProfile import label
import numpy as np
import streamlit as st
import pandas as pd
import altair as alt
import pydeck as pdk  # For map visualization
import geopandas as gpd
import matplotlib.pyplot as plt
from dutchdict import Themes
from test_dutch import file_options 
import folium
from folium.plugins import HeatMap
from streamlit.components.v1 import iframe
import json

# Page configuration
st.set_page_config(
    page_title="Broad Prosperity: Netherlands",
    layout="wide",
    initial_sidebar_state="expanded")

st.markdown("""
    <div style='text-align: left; padding: 10px;'>
        <h1 style='color: #eb1d9c; font-size: 48px; font-weight: bold; margin-bottom: 0;'> cmo stamm.</h1>
        <h2 style='color: black; font-size: 32px; font-weight: bold; margin-top: 0;'>Brede welvaart van het Nederland</h2>
    </div>
    """, unsafe_allow_html=True)

    #######################
    # CSS styling
st.markdown("""
    <style>
    /* Customize sidebar */
    [data-testid="stSidebar"] {
        background-color: #149bed; /* blue background */
        padding: 10px; /* Add some padding for neatness */
    }
                
    [data-testid="stSidebar"] h1 {
        color: #ffffff; /* Customize white sidebar title color */
        font-weight: bold;
    }

    .stApp [data-testid="block-container"] {
        padding-left: 0rem;
        padding-right: 0rem;
        padding-top: 0rem;
        padding-bottom: 0rem;
        margin-bottom: -7rem;
        background-color: #cce1ee !important; /* Light blue background */
    }
                
    .st-expander .streamlit-expanderContent {
            color: #FFFFFF;  /* Example color for the content text */
        }
    </style>
    """, unsafe_allow_html=True)

#######################
# Load data
#df_meta = pd.read_csv('meta.csv')
df_indicators = pd.read_csv('indmaarmunn.csv')
df_thema = pd.read_excel('thematicpath.xlsx')

#######################
# Sidebar
with st.sidebar:
    st.title('Indicatoren van brede welvaart')
    # Check if df_indicators is a DataFrame and contains 'label'
    type = st.radio("what would you like to visualise ?",
        ["Themes", "Indicators"],
        captions = [
            "Overall themes",
            "Indicators within the themes"
        ],)

    if type == "Themes":
        options = df_thema["Thema"].dropna().unique().tolist()
    else:
        options = file_options


    selected_indicator = st.selectbox("Select a Theme/an Indicator:", options)

    jaar = df_indicators['jaar'].dropna().unique().tolist()
    
    year_columns = file_options[selected_indicator]["year_columns"]
    selected_year = st.selectbox("Selecteer een jaar:", list(year_columns.keys()))

#######################
# Dashboard Main Panel
col0 = st.columns((5, 3), gap='medium')

with col0[0]:
    #Extract path, year_columns, and title based on selection
    indicator_path = file_options[selected_indicator]["path"]
    title_base = file_options[selected_indicator]["title"]

    # Load the selected file
    indicator = gpd.read_file(indicator_path)

    # Get the column corresponding to the selected year
    selected_column = year_columns[selected_year]
    
    # **2. Interactive pydeck Map**
    # Ensure geometry is valid
    indicator = indicator[indicator.geometry.notnull()]

    # Get the column corresponding to the selected year
    selected_column = year_columns[selected_year]

    # Convert non-JSON serializable types (e.g., Timestamps) to strings
    for column in indicator.columns:
        if pd.api.types.is_datetime64_any_dtype(indicator[column]):
            indicator[column] = indicator[column].dt.strftime('%Y-%m-%d')

    # Handle missing values: Set them to NaN and assign them a white color later
    indicator[selected_column] = pd.to_numeric(indicator[selected_column], errors='coerce')

    # Calculate quantiles
    quantiles = indicator[selected_column].quantile([0.0, 0.25, 0.5, 0.75, 1.0]).values

    # Function to assign colors based on quantile
    def get_color(value):
        if pd.isna(value):
            return [255, 0, 0]  # Red for missing values
        elif value <= quantiles[1]:  # 0-25% quantile range
            return [228, 239, 209]  
        elif value <= quantiles[2]:  # 25-50% quantile range
            return [152, 197, 194]  
        elif value <= quantiles[3]:  # 50-75% quantile range
            return [73, 127, 153]  
        else:  # 75-100% quantile range
            return [44, 86, 124]  
    # Apply the color function to each feature
    indicator["fill_color"] = indicator[selected_column].apply(get_color)

    # Prepare data for hover interaction
    indicator["hover_info"] = indicator.apply(lambda row: f"{row['statnaam']}: {row[selected_column]}", axis=1)

    # Add hover functionality using Streamlit
    indicator = indicator.to_crs(epsg=4326)  # Ensure GeoDataFrame is in WGS84 for PyDeck

    # Serialize GeoJSON manually to handle custom hover_info and fill_color
    geojson_data = json.loads(indicator.to_json())
    for feature, hover_text, fill_color in zip(geojson_data["features"], indicator["hover_info"], indicator["fill_color"]):
        feature["properties"]["hover_info"] = hover_text
        feature["properties"]["fill_color"] = fill_color

    # Create PyDeck layer with dynamic colors
    layer = pdk.Layer(
        "GeoJsonLayer",
        data=geojson_data,
        pickable=True,
        get_fill_color="properties.fill_color",
        get_line_color="[255, 255, 255]",
        line_width_min_pixels=1,
        auto_highlight=True,
    )

    # Create PyDeck map
    view_state = pdk.ViewState(
        latitude=indicator.geometry.centroid.y.mean(),
        longitude=indicator.geometry.centroid.x.mean(),
        zoom=6
    )

    r = pdk.Deck(layers=[layer], initial_view_state=view_state, tooltip={"html": "<b>{hover_info}</b>"})

    # Display the map with Streamlit
    st.pydeck_chart(r)

st.write("Welkom bij het hoofddashboard. Gebruik de knop hierboven om te navigeren.")
        
with col0[1]:

    st.markdown(f'**Wat is Brede Welvaart ?**')

    st.markdown('''
    Brede welvaart gaat over alles wat het leven ‘de moeite waard maakt’. 
    Het gaat over inkomen en werk, maar ook over de woonkwaliteit, natuur, 
    gezondheid en het welbevinden van mensen. Dat is het uitgangspunt achter het concept 
    ‘brede welvaart’. Het is een andere manier van kijken naar de samenleving. Integraal, 
    met oog voor de samenhang tussen de factoren die er voor de inwoners toe doen.
    ''')
    st.markdown('''
    CMO STAMM werkt aan de verbetering van de brede welvaart in het Noorden. Dit doen 
    wij door bewustwording te vergroten, het monitoren en uitvoeren van onderzoek en het 
    ontwikkelen van een visie en strategie voor beleid.
    ''')

    if selected_indicator:
        st.markdown(Themes[selected_indicator])

    st.expander('About', expanded=True)

    df_indicators['jaar'] = df_indicators['jaar'].astype(str)  # Convert to string
    selected_year = str(selected_year)  # Convert selected year to string

    df_selectedindicator = df_indicators[
        (df_indicators['label'] == selected_indicator)&
        (df_indicators['jaar'] == selected_year)]

    df_selectedindicator_sorted = df_selectedindicator.sort_values(by='waarde', ascending=True)
    
    columns_to_include = ['statnaam', 'waarde'] 
    
    df_selectedindicator_sorted = df_selectedindicator_sorted[columns_to_include]

    st.markdown(f'**Gemeenten gerangschikt van hoog naar laag in {selected_indicator}**')

    if df_selectedindicator_sorted.empty:
            st.warning("Geen gegevens beschikbaar voor de geselecteerde indicator.")
    else:
        # Display the DataFrame using Streamlit
        st.dataframe(
        df_selectedindicator_sorted, 
        column_order=("statnaam", "waarde"), 
        hide_index=True, 
        width=None, 
        column_config={
            "statnaam": st.column_config.TextColumn(
                "Statnaam",
            ),
            "waarde": st.column_config.TextColumn(
                "Waarde",  # This will now display as plain numbers
            ),
        }
    )
    with st.expander('About', expanded=True):
        st.write('''
            - Data: [CBS data: Nederland (https://www.cbs.nl/nl-nl/visualisaties/regionale-monitor-brede-welvaart/indicator)]''')
st.markdown("""
    <div style='text-align: left; padding: 10px; display: flex; align-items: center;'>
        <h1 style='color: #e5007d; font-size: 20px; font-weight: bold; margin-top: 0; margin-right: 8px;'>For the Dutch page:</h1>
        <a href="https://broad-prosperity-dashboard.streamlit.app" target="_blank" style="
            text-decoration: none;
            background-color: #e5007d;
            color: white;
            padding: 6px 12px;
            border-radius: 5px;
            font-size: 14px;
            font-weight: bold;
            margin-left: -5px;
        ">Click here</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div style='text-align: left; padding: 10px; display: flex; align-items: center;'>
        <h1 style='color: #e5007d; font-size: 20px; font-weight: bold; margin-top: 0; margin-right: 8px;'>For the download page:</h1>
        <a href="https://streamlit.io/gallery" target="_blank" style="
            text-decoration: none;
            background-color: #e5007d;
            color: white;
            padding: 6px 12px;
            border-radius: 5px;
            font-size: 14px;
            font-weight: bold;
            margin-left: -5px;
        ">Click here</a>
    </div>
    """, unsafe_allow_html=True)
