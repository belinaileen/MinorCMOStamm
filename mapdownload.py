import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import pydeck as pdk
from test_dutch import file_options
from Cmon import selected_indicator
from Cmon import selected_year

df_indicators = pd.read_csv('indmaarmunn.csv')

with st.sidebar:
    st.title("Broad Prosperity Indicators")

col = st.columns((2,1), gap='medium')
#  map
with col[0]:
    # Dropdown menu for selecting the year
    file_info = file_options[selected_indicator]
    year_columns = file_info["year_columns"]

    selected_column = year_columns[selected_year]

    indicator_path = file_info["path"]
    title_base = file_info["title"]

    # Load the selected file
    indicator = gpd.read_file(indicator_path)

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
            legend_kwds={'orientation': 'vertical'}
        )
        plt.title(f"{title_base} van Nederland in {selected_year}")

        # Display the figure in Streamlit
        st.pyplot(fig)
    else:
        # If the column is not available, show a message
        st.write(f"Data is unavailable for the year {selected_year}.")

with col[1]:
    st.write("Deze pagina is bedoeld voor het downloaden van de kaarten als afbeeldingen.")
    st.write("Zorg ervoor dat je de gewenste indicator en het gewenste jaar selecteert en klik vervolgens met de rechtermuisknop op de kaart en kies Afbeelding opslaan als...")
    
st.markdown("""
    <div style='text-align: left; padding: 10px; display: flex; align-items: center;'>
        <h1 style='color: #e5007d; font-size: 20px; font-weight: bold; margin-top: 0; margin-right: 8px;'>For the download page:</h1>
        <a href="https://cmostamm.streamlit.app/" target="_blank" style="
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




