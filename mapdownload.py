import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import pydeck as pdk
from path_dutch import file_options_indicators
from path_dutch import file_options_themes
from dutchdict import Themes # A custom dictionary providing thematic descriptions
from dutchdict import Expander
from path_dutch import color_schemes # A dictionary for color schemes
import matplotlib.colors as mcolors

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
df_indicators = pd.read_csv('indmaarmunn.csv')
#######################
# Sidebar
with st.sidebar:
    st.title('Indicatoren van brede welvaart')
    # Check if df_indicators is a DataFrame and contains 'label'
    type = st.radio("Wat zou je willen visualiseren?",
        ["Themes", "Indicators"],
        captions = [
            "Algemene thema's",
            "Indicatoren binnen de thema's"
        ],)

    if type == "Themes":
        options = file_options_themes
    else:
        options = file_options_indicators

    selected_indicator = st.selectbox("Select a Theme/an Indicator:", options)

    jaar = df_indicators['jaar'].dropna().unique().tolist()
    # Dropdown menu for selecting the year
    file_info = options[selected_indicator]
    year_columns = file_info["year_columns"]
    selected_year = st.selectbox("Selecteer een jaar:", list(year_columns.keys()))

    selected_scheme = st.selectbox("Select a a color scheme", color_schemes.keys())

#######################
# Dashboard Main Panel
col0 = st.columns((5, 3), gap='medium')

with col0[0]:
    #Extract path, year_columns, and title based on selection
    indicator_path = options[selected_indicator]["path"]
    title_base = file_info["title"]

    # Load the selected file
    indicator = gpd.read_file(indicator_path)

    # Get the column corresponding to the selected year
    selected_column = year_columns[selected_year]
    
    # Handle missing values: Set them to NaN and assign them a white color later
    indicator[selected_column] = pd.to_numeric(indicator[selected_column], errors='coerce')
    
    # Calculate quantiles
    quantiles = indicator[selected_column].quantile([0.0, 0.25, 0.5, 0.75, 1.0]).values
    
    # Function to assign colors based on quantile
    def get_color(value):
        if pd.isna(value):
            return selected_scheme[0]#for missing values
        elif value <= quantiles[1]:  # 0-25% quantile range
            return selected_scheme[1] 
        elif value <= quantiles[2]:  # 25-50% quantile range
            return selected_scheme[2] 
        elif value <= quantiles[3]:  # 50-75% quantile range
            return selected_scheme[3]
        else:  # 75-100% quantile range
            return selected_scheme[4]

    # Convert the RGB values from 0-255 to 0-1 scale
    def create_colormap(rgb_list):
        norm_rgb_list = [[r/255, g/255, b/255] for r, g, b in rgb_list]
        return mcolors.ListedColormap(norm_rgb_list)
        
    # Ensure selected_scheme is a valid colormap
    if selected_scheme in color_schemes:
        cmap = create_colormap(color_schemes[selected_scheme])
    else:
        cmap = "Blues"  # Default to a valid Matplotlib colormap
    
    # Check if the selected column exists
    if selected_column in indicator.columns:
        fig = plt.figure(figsize=[12, 8])
        ax = fig.add_axes([0, 0, 1, 1])
    
        # Plot with the converted colormap
        indicator.plot(
            column=selected_column,
            ax=ax,
            legend=True,
            cmap=cmap,  
            legend_kwds={'orientation': 'vertical'}
        )
        
        plt.title(f"{title_base} van Nederland in {selected_year}")
    
        # Display the figure in Streamlit
        st.pyplot(fig)
    else:
        st.write(f"Gegevens zijn niet beschikbaar voor het jaar")

    if selected_indicator:
        st.markdown(Themes[selected_indicator])
    with st.expander(f'Meer Informatie'):
        if selected_indicator:
            st.write(Expander[selected_indicator])

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

    with st.expander('Ongeveer', expanded=True):
        st.write('''
            - Data: [CBS data: Nederland (https://www.cbs.nl/nl-nl/visualisaties/regionale-monitor-brede-welvaart/indicator)]''')

st.markdown(""" <div style='text-align: left; padding: 10px; display: flex; align-items: center;'>
    <h1 style='color: #e5007d; font-size: 20px; font-weight: bold; margin-top: 0; margin-right: 8px;'>Terug naar de Nederlandse pagina:</h1>
    <a href="https://bp-dashboard-dutch.streamlit.app/" target="_blank" style="
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
