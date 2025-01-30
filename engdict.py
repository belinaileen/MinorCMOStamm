# Define the themes and their corresponding markdown content

Themes = {
    "Average debt per household": """
        **Welcome to the Average Household Debt indicator**
        - This indicator is part of the Economic Capital theme.
        - 2022 figures are preliminary, and the adjustment for price changes 
        in 2021 and 2022 is based on the consumer price research series, which 
        uses actual energy prices paid. This aligns more closely with the price 
        developments experienced by the population than the consumer price index.
        - Measuring unit: Euro average debt per household
    """,
    "Built up area": """
        **Welcome to the Built-up Area indicator**
        - This indicator is part of the Natural Capital theme.
        - Measuring unit: Percentage of land area
    """,
    "Contact with family, friends or neighbors": """
        **Welcome to the Contact with Family, Friends, or Neighbors indicator**
        - This indicator is part of the Society theme.
        - Preliminary figures. When a new year is added, the model re-estimates 
        all years in the series. Refer to the Technical Explanation for more 
        details on interpreting model estimates and margins.
        - Measuring unit: Percentage of population aged 15+ has contact at least once a week on average
    """,
    "Distance to café etc.": """
        **Welcome to the Distance to Café, etc. indicator**
        - This indicator is part of the Distance and Living Facilities theme. It measures the average distance residents 
        travel to access cafés and similar establishments, assuming a 4.184 km travel distance. Using 
        municipal data and spatial analysis in ArcGIS Pro, distances are adjusted to account for neighboring 
        municipalities. If spillover effects suggest a greater distance than the original municipal value, 
        the original value is retained.
        - Measuring unit: Kilometers
    """,
    "Distance to primary school": """
        **Welcome to the Distance to Primary School indicator**
        - This indicator is part of the Distance to Living Facilities theme. It measures the average distance 
        residents travel to access a primary school, assuming a 4.023 km travel distance. Using municipal data 
        and spatial analysis in ArcGIS Pro, distances are adjusted to account for neighboring municipalities. 
        If spillover effects suggest a greater distance than the original municipal value, the original value 
        is retained.
        - Measuring unit: Kilometers
    """,
    "Distance to public green areas": """
        **Welcome to the Distance to Public Green Areas indicator**
        - This indicator is part of the Environment theme, in the Nature sub-theme. It measures the average 
        distance residents travel to access public green spaces, assuming a 1.65 km travel distance. 
        Using municipal data and spatial analysis in ArcGIS Pro, distances are adjusted to account for 
        neighboring municipalities. If spillover effects suggest a greater distance than the original 
        municipal value, the original value is retained.
        - Measuring unit: Kilometers
    """,
    "Distance to public transportation": """
        **Welcome to the Distance to Public Transport indicator**
        - This indicator is part of the Labor and Free Time theme.
        -It measures the average distance residents travel to access public transportation, 
        considering a 791-meter assumed travel distance. Using municipal data and
        spatial analysis in ArcGIS Pro, distances are adjusted to account for neighboring
        municipalities. If spillover effects suggest a greater distance than the original
        municipal value, the original value is retained.
        - Measuring unit: Kilometers
    """,
    "Distance to sports field": """
        **Welcome to the Distance to Sports Facility indicator**
        - This indicator is part of the Labor and Free Time theme.
        -It measures the average distance residents travel to access sports fields, 
        assuming a 1 km travel distance. Using municipal data and spatial analysis in ArcGIS Pro, 
        distances are adjusted to account for neighboring municipalities. 
        If spillover effects suggest a greater distance than the original municipal value, 
        the original value is retained.
        - Measuring unit: Kilometers
    """,
    "Emissions of particulate matter to air": """
        **Welcome to the Emissions of Particulate Matter to Air indicator**
        - This indicator is part of the Environment theme, in the Air Quality and Natural Capital sub-themes. 
        It measures the emissions of particulate matter (PM₂.₅) to air, assuming a 500-meter spillover distance
        to reflect regional dispersion. Using municipal data and spatial analysis in ArcGIS Pro,
        values are adjusted to account for neighboring municipalities. If spillover effects suggest
        a greater emission value than the original municipal value, the original value is retained.
        - Measuring unit: kg PM₂.₅ per km²
    """,
    "Experienced health": """
        **Welcome to the Experienced Health indicator**
        - This indicator is part of the Health theme.
        - For the years 2012 and 2016, the measured population is 19+.
        - Measuring unit: Percentage of the population aged 18+ consider their own health to be (very) good
    """,
    "Greenhouse gas emissions per capita": """
        **Welcome to the Greenhouse Gas Emissions per Inhabitant indicator**
        - This indicator is part of the Environment theme.
        - The entire series has been adjusted due to new IPCC guidelines.
        - Measuring unit: Tonnes of CO2 equivalent per inahbitant
    """,
    "Life expectancy of the population": """
        **Welcome to the Life Expectancy of the Population indicator**
        - This indicator is part of the Health theme.
        - Average life expectancy over the period 2018-2021, not determined 
        separately per year.
        - Measuring unit: The life expentancy in years at birth
    """,
    "Median disposable income": """
        **Welcome to the Median Disposable Income indicator**
        - This indicator is part of the Material Well-being theme.
        - 2021 figures are preliminary, and the adjustment for price changes in 
        2021 is based on the consumer price research series, which uses actual 
        energy prices paid. This aligns more closely with the price developments 
        experienced by the population than the consumer price index.
        - Measuring unit: Euro per household corrected for inflation, in constant 2021 prices
    """,
    "Median household wealth": """
        **Welcome to the Median Household Wealth indicator**
        - This indicator is part of the Economic Capital theme.
        - 2021 figures are preliminary, and the adjustment for price changes 
        in 2021 is based on the consumer price research series, which uses 
        actual energy prices paid. This aligns more closely with the price 
        developments experienced by the population than the consumer price index.
        - Measuring unit: Euro
    """,
    "Nature and forest areas": """
        **Welcome to the Nature and Forest Areas indicator**
        - This indicator is part of the Environment theme, in the Nature and Natural Capital sub-themes.
        It measures the percentage of municipal surface area covered by nature and forests, assuming a 1.65 km
        spillover distance. Using municipal data and spatial analysis in ArcGIS Pro, values are adjusted to
        account for neighboring municipalities. If spillover effects suggest a greater percentage than
        the original municipal value, the original value is retained.
        - Measuring unit: Percentage of surface area
    """,
    "Nature area per inhabitant": """
        **Welcome to the Nature Area per Inhabitant indicator**
        - This indicator is part of the Environment theme, in the Nature sub-theme. It measures the amount 
        of nature area per 1,000 inhabitants, assuming a 1.65 km spillover distance to reflect regional 
        accessibility. Using municipal data and spatial analysis in ArcGIS Pro, values are adjusted to account
        for neighboring municipalities. If spillover effects suggest a greater value than the original 
        municipal value, the original value is retained.
        - Measuring unit: Square meters per 1000 inhabitants
    """,
    "Net labor particiption" : """
        **Welcome to the Net Labor Participation indicator**
        - This indicator is part of Labor and Free Time theme. It measures the percentage of individuals participating in the labor force,
        assuming a 25 km spillover distance to reflect regional influence. Due to data limitations,
        calculations use the working population aged 15 to 64. Using municipal data and spatial analysis in ArcGIS Pro,
        values are adjusted to account for neighboring municipalities. If spillover effects suggest a greater percentage 
        than the original municipal value, the original value is retained.
        - Measuring unit: Percentage of the working population
    """,
    "Number of crimes encountered": """
        **Welcome to the Number of Crimes Encountered indicator**
        - This indicator is part of the Safety theme.
        - Measuring unit: Number of crimes experienced per 100 inhabitants
    """,
    "Overweight": """
        **Welcome to the Overweight indicator**
        - This indicator is part of the Health theme.
        - For the year 2016, the measured population is 19+.
        - Measuring unit: Percentage of the population aged 18+ is overweight
    """,
    "Population with a starting qualification": """
        **Welcome to the Population with a Starting Qualification indicator**
        - This indicator is part of the Labor and Free Time theme. It measures the percentage of individuals 
        aged 15 to 74 with a starting qualification, using a 25 km spillover distance to reflect regional 
        influence. Due to data limitations, calculations are based on the working population (aged 15 to 64). 
        Spatial analysis in ArcGIS Pro accounts for municipal spillovers and adjusts the values accordingly.
        - Measuring unit: Percentage of the population with a starting qualification
    """,
    "Private solar energy": """
        **Welcome to the Private Solar Energy indicator**
        - This indicator is part of the Natural Capital sub-theme. 
        It measures private solar energy production per household, assuming a 1 km spillover distance to
        reflect regional influence. Using municipal data and spatial analysis in ArcGIS Pro,
        values are adjusted to account for neighboring municipalities. If spillover effects suggest
        a greater value than the original municipal value, the original value is retained.
        - Measuring unit: Watts per home
    """,
    "Recorded crimes": """
        **Welcome to the Recorded Crimes indicator**
        - This indicator is part of the Safety theme.
        - 2021 and 2022 figures are preliminary.
        - Measuring unit: Registered crimes per 1000 inhabitants
    """,
    "Registered problematic debt": """
        **Welcome to the Registered Problematic Debt indicator**
        - This indicator is part of the Economic Capital theme.
        - Measuring unit: Number of registered problematic debts
    """,
    "Satisfaction with free time": """
        **Welcome to the Satisfaction with free time indicator**
        - This indicator is part of the Subjective Well-being theme.
        - Preliminary figures. When a new year is added, the model re-estimates 
        all years in the series. Refer to the Technical Explanation for more 
        details on interpreting model estimates and margins.
        - Measuring unit: Percentage of the population aged 18+ is (very) satisfied
    """,
    "Satisfaction with housing": """
        **Welcome to the Satisfaction with Housing indicator**
        - This indicator is part of the Housing theme.
        - Measuring unit: Percentage of private households are (very) satisfied
    """,
    "Satisfaction with life": """
        **Welcome to the Life Satisfaction indicator**
        - This indicator is part of the Subjective Well-being theme.
        - Preliminary figures. When a new year is added, the model re-estimates 
        all years in the series. Refer to the Technical Explanation for more 
        details on interpreting model estimates and margins.
        - Measuring unit: Percentage of Dutch people give life a 7 or higher
    """,
    "Satisfaction with living environment": """
        **Welcome to the Satisfaction with Living Environment indicator**
        - This indicator is part of the Housing theme.
        - Measuring unit: Percentage of private households are (very) satisfied
    """,
    "Satisfaction with social life": """
        **Welcome to the Satisfaction with Social Life indicator**
        - This indicator is part of the Subjective Well-being theme.
        - Measuring unit: Percentage of the population satisfied with their social life
    """,
    "Social cohesion": """
        **Welcome to the Social Cohesion indicator**
        - This indicator is part of the Social Capital theme.
        - Measuring unit: Scale score (0-10)
    """,
    "Trust in institutions": """
        **Welcome to the Trust in Institutions indicator**
        - This indicator is part of the Society theme. It measures the percentage of the population aged 15 
        and older who have sufficient trust in institutions, with a 41.05 km spillover distance reflecting 
        regional influence. Using municipal data and spatial analysis in ArcGIS Pro, trust levels are adjusted 
        to account for neighboring municipalities while considering population size.
        - Measuring unit: Percentage of the population aged 15+ has sufficient confidence in institutions.
    """,
    "Trust in others": """
        **Welcome to the Trust in Others indicator**
        - This indicator is part of the Society theme. It measures the percentage of the population aged 15 
        and older who have sufficient trust in others, with a 41.05 km spillover distance reflecting regional 
        influence. Using municipal data and spatial analysis in ArcGIS Pro, trust levels are adjusted to
        account for neighboring municipalities while considering population size.
        - Measuring unit: Percentage of population aged 15+ find most people trustworthy
    """,
    "Unemployment": """
        **Welcome to the Unemployment indicator**
        - This indicator is part of the Labor and Free Time theme. It measures the percentage of 
        the working population who are unemployed, with a 25 km spillover distance reflecting regional
        influence. Using municipal data and spatial analysis in ArcGIS Pro, unemployment levels are adjusted to
        account for neighboring municipalities while considering population size.
        - Measuring unit: Percentage of the working population
    """,
    "Volunteer work": """
        **Welcome to the Volunteering indicator**
        - This indicator is part of the Society theme.
        - Preliminary figures. When a new year is added, the model re-estimates 
        all years in the series. Refer to the Technical Explanation for more 
        details on interpreting model estimates and margins.
        - Measuring unit: Percentage of population aged 15 and over doing organised volunteer work in the current year
    """,
    "Often feeling unsafe in the neighborhood": """
        **Welcome to the Often Feeling Unsafe in the Neighborhood indicator**
        - This indicator is part of the Safety theme.
        - Measuring unit: Percentage of the population aged 15+ that often feels unsafe.
    """,
    "People with one or more longterm illnesses or conditions": """
        **Welcome to the People with one or more long-term illnesses or conditions indicator**
        - This indicator is part of the Health theme.
        - For the years 2012 and 2016, the measured population is 19+.
        - Measuring unit: Percentage of population aged 18 years or older
    """,
    "Quality of bathing water coastal waters": """
        **Welcome to the Quality of Swimming Water in Coastal Waters indicator**
        - This indicator is part of the Environment theme. It measures the average quality of 
        coastal bathing water, assuming a 1.65 km spillover distance. Using municipal data and 
        spatial analysis in ArcGIS Pro, quality values are adjusted to account for neighboring municipalities.
        This ensures that the indicator reflects regional influences on water quality beyond municipal borders.
        - Measuring unit: Quality score (1=poor to 4=excellent)
    """,
    "Quality of inland bathing water": """
        **Welcome to the Quality of Swimming Water in Inland Waters indicator**
        - This indicator is part of the Environment theme. It measures the average quality of inland 
        bathing water, assuming a 1.65 km spillover distance. Using municipal data and spatial analysis
        in ArcGIS Pro, quality values are adjusted to account for neighboring municipalities. 
        This ensures that the indicator reflects regional influences on water quality beyond municipal borders.
        - Measuring unit: Quality score (1=poor to 4=excellent)
    """,
    "Air quality": """
        **Welcome to the Air Quality theme**
        - In this theme, the following indicators are included: Emissions of particulate matter to air, Greenhouse gas emissions per capita
    """,
    "Distance to living facilities": """
        **Welcome to the Distance to Living Facilities theme**
        - In this theme, the following indicators are included: ....
    """,
    "Environment": """
        **Welcome to the Environment theme**
        - In this theme, the following indicators are included: Nature area per inhabitant, Emissions of particulate matter to air, 
        Nature and forest areas, Distance to public green areas, Greenhouse gas emissions per capita, 
        Quality of inland bathing water, Quality of coastal bathing water
    """,
    "Health": """
        **Welcome to the Health theme**
        - In this theme, the following indicators are included: Overweight, Experienced Health, 
        Life expectancy of the population, People with one or more long-term illnesses or conditions
    """,
    "Labor and free time": """
        **Welcome to the Labor and Free Time theme**
        - In this theme, the following indicators are included: Net labor participation, Gross labor participation, 
        Highly educated population, Unemployment, Vacancy rate
    """,
    "Material welfare and economic capital": """
        **Welcome to the Material Welfare and Economic Capital theme**
        - In this theme, the following indicators are included: Median disposable income, Gross domestic product, 
        Average debt per household, Median household wealth
    """,
    "Natural capital": """
        **Welcome to the Natural Capital theme**
        - In this theme, the following indicators are included: Private solar energy, Nature and forest areas, Built environment, 
        Emissions of particles, Green-blue infrastructure
    """,
    "Nature": """
        **Welcome to the Nature theme**
        - In this theme, the following indicators are included: ....
    """,
    "Society": """
        **Welcome to the Society theme**
        - In this theme, the following indicators are included: Contact with family, friends, or neighbors, 
        Trust in institutions, Trust in others, Volunteer work
    """,
    "Well-being": """
        **Welcome to the Well-being theme**
        - In this theme, the following indicators are included: Satisfaction with life, Satisfaction with free time
    """,
}