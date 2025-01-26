import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import pydeck as pdk
from test import file_options

def render():
    try:
        names = pd.read_csv('indmaarmunn.csv')
    except FileNotFoundError:
        st.error("Error: 'selected_column.xlsx' not found.")
        st.stop()

    with st.sidebar:
        st.title("Broad Prosperity Indicators")

        options = names['label'].dropna().unique().tolist()
        selected_indicator = st.selectbox("Selecteer een Indicator", options)

        file_info = file_options[selected_indicator]
        year_columns = file_info["year_columns"]
        selected_year = st.selectbox("Selecteer een jaar:", list(year_columns.keys()))

    col = st.columns((2,1), gap='medium')
    #  map
    with col[0]:

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
        
    # Check if the "Go Back" button is clicked
    if st.button("Go Back"):
        # Set query parameters to redirect to the "Home" page
        st.experimental_set_query_params(page="Home")


