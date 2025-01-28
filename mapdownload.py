import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import pydeck as pdk
from test_dutch import file_options

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
    type = st.radio("Wat zou je willen visualiseren?",
        ["Thema's", "Indicatoren"],
        captions = [
            "Algemene thema's",
            "Indicatoren binnen de thema's"
        ],)

    if type == "Themes":
        options = df_thema["Thema"].dropna().unique().tolist()
    else:
        options = file_options


    selected_indicator = st.selectbox("Select a Theme/an Indicator:", options)

    jaar = df_indicators['jaar'].dropna().unique().tolist()
    # Dropdown menu for selecting the year
    file_info = file_options[selected_indicator]
    year_columns = file_info["year_columns"]
    selected_year = st.selectbox("Selecteer een jaar:", list(year_columns.keys()))

#######################
# Dashboard Main Panel
col0 = st.columns((5, 3), gap='medium')

with col0[0]:
    #Extract path, year_columns, and title based on selection
    indicator_path = file_options[selected_indicator]["path"]
    title_base = file_info["title"]

    # Load the selected file
    indicator = gpd.read_file(indicator_path)

    # Get the column corresponding to the selected year
    selected_column = year_columns[selected_year]

    # Check if the selected column exists in the data
    if selected_column in indicator.columns:
        # **1. Static Plot using Matplotlib**
        # Create a Matplotlib figure
        fig = plt.figure(figsize=[12, 8])
        ax = fig.add_axes([0, 0, 1, 1])
        indicator.plot(
            column=selected_column,
            ax=ax,
            legend=True,
            cmap="blues",
            legend_kwds={'orientation': 'vertical'}
        )
        plt.title(f"{title_base} van Nederland in {selected_year}")

        # Display the figure in Streamlit
        st.pyplot(fig)
    else:
        # If the column is not available, show a message
        st.write(f"Gegevens zijn niet beschikbaar voor het jaar")
        
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
        st.markdown('**Welkom bij{selected_indicator}**')

    st.expander('About', expanded=True)
    df_indicators['jaar'] = df_indicators['jaar'].astype(str)  # Convert to string
    selected_year = str(selected_year)  # Convert selected year to string

    df_selectedindicator = df_indicators[
        (df_indicators['label'] == selected_indicator)&
        (df_indicators['jaar'] == selected_year)]

    df_selectedindicator_sorted = df_selectedindicator.sort_values(by='waarde', ascending=False)
    
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

st.markdown(""" <div style='text-align: left; padding: 10px; display: flex; align-items: center;'>
    <h1 style='color: #e5007d; font-size: 20px; font-weight: bold; margin-top: 0; margin-right: 8px;'>Terug naar de Nederlandse pagina:</h1>
    <a href="https://cmostammdutch.streamlit.app/" target="_blank" style="
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
