import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
import json
import pydeck as pdk

# mission years and columns
# Satisfaction with Social life
# Registered Problematic Debt
# Population with Starting Qualification
# Emissions particulate matter

# Define the file options and their year-to-fieldname mappings
file_options_indicators = {
    "Mediaan besteedbaar inkomen": {
        "year_columns": {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        "path": 'MedianDisposableIncome.geojson',
        "title": "Mediaan besteedbaar inkomen",
    },
    "Tevredenheid met het leven": {
        "path": r"SatisfactionLife.geojson",
        "year_columns": {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        "title": "Tevredenheid met het leven",
    },
    "Tevredenheid met vrije tijd": {
        "path": r"SatisfactionFreeTime.geojson",
        "year_columns": {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        "title": "Tevredenheid met vrije tijd",
    },  
    "Overgewicht": {
        "path": r"Overweight.geojson",
        "year_columns": {
            '2016': 'Year2016',
            '2020': 'Year2020',
            '2022': 'Year2022',
        },
        "title": "Overgewicht",
    },
    "Ervaren gezondheid": {
        "path": r"ExperiencedHealth.geojson",
        "year_columns": {
            '2016': 'Year2016',
            '2020': 'Year2020',
            '2022': 'Year2022',
        },
        "title": "Ervaren gezondheid",
    },
    "Levensverwachting bevolking": {
        "path": r"LifeExpectancyOfThePopulation.geojson",
        "year_columns": {
            '2022': 'Year2022',
        },
        "title": "Levensverwachting bevolking",
    },
    "Personen met één of meer langdurige ziekten of aandoeningen": {
        "path": r"PeopleWithIllness.geojson",
        "year_columns": {
            "2016": "Year2016",
            "2020": "Year2020",
            "2022": "Year2022",
        },
        "title": "Personen met één of meer langdurige ziekten of aandoeningen",
    },
    "Nettoarbeidsparticipatie": {
        "path": r"NetLaborParticipation.geojson",
        "year_columns": {
            "2013": "Year2013",
            "2014": "Year2014",
            "2015": "Year2015",
            "2016": "Year2016",
            "2017": "Year2017",
            "2018": "Year2018",
            "2019": "Year2019",
            "2020": "Year2020",
            "2021": "Year2021",
            "2022": "Year2022",

        },
        "title": "Nettoarbeidsparticipatie",
    },
    "Werkloosheid": {
        "year_columns": {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        "path": r"Unemployment.geojson",
        "title": "Werkloosheid",
    },
    # Distance to public transport - move to GitHub
    "Afstand tot ov": {
        "path": r"DistanceToPublicTransportation.geojson",
        "year_columns": {
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        "title": "Afstand tot ov",
    },
    "Tevredenheid met woonomgeving": {
        "path": r"SatisfactionLivingEnvironment.geojson",
        "year_columns": {
            '2015': 'Year2015',
            '2018': 'Year2018',
            '2021': 'Year2021',
        },
        "title": "Tevredenheid met woonomgeving",
    },
    "Tevredenheid met woning": {
        "year_columns": {
            '2015': 'Year2015',
            '2018': 'Year2018',
            '2021': 'Year2021',
        },
        "path": r"SatisfactionHousing.geojson",
        "title": "Tevredenheid met woning",
    },
    "Afstand tot sportterrein": {
        "path": r"DistanceToSportsField.geojson",
        "year_columns": {
            '2015': 'Year2015',
            '2017': 'Year2017',
        },
        "title": "Afstand tot sportterrein",
    },
    # Distance to Primary school - move to GitHub
    "Afstand tot basisschool": {
        "path": r"DistanceToPrimarySchool.geojson",
        "year_columns": {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        "title": "Afstand tot basisschool",
    },
    # Distance to cafe - move to GitHub
    "Afstand tot café e.d.": {
        "path": r"DistanceToCafe.geojson",
        "year_columns": {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
        },
        "title": "Afstand tot café e.d.",
    },
    # Contact with family, friends or neighbors 
    "Contact met familie, vrienden of buren": {
        "path": r"ContactWithFamilyEtc.geojson",
        "year_columns": {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
        },
        "title": "Contact met familie, vrienden of buren",
    },
    "Vertrouwen in instituties": {
        "path": r"TrustInstitutions.geojson",
        "year_columns": {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        "title": "Vertrouwen in instituties",
    },
    "Vertrouwen in anderen": {
        "path": r"TrustOthers.geojson",
        "year_columns": {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
    },
        "title": "Vertrouwen in anderen",
    "Vrijwilligerswerk": {
        "year_columns": {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        "path": r"VolunteerWork.geojson",
        "title": "Vrijwilligerswerk",
    },
    # often feeling unsafe in neighborhood
    "Vaak onveilig gevoel in de buurt": {
        "path": r"OftenFeelingUnsafe.geojson",
        "year_columns": {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2019': 'Year2019',
            '2021': 'Year2021',
            '2023': 'Year2023',
        },
        "title": "Vaak onveilig gevoel in de buurt",
    },
    "Aantal ondervonden delicten": {
        "path": r"Update_Number_crimes_encountered.geojson",
        "year_columns": {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2019': 'Year2019',
            '2021': 'Year2021',
            '2023': 'Year2023',
        },
        "title": "Aantal ondervonden delicten",
    },
    "Geregistreerde misdrijven": {
        "year_columns": {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        "path": r"Update_Recorded_crimes.geojson",
        "title": "Geregistreerde misdrijven",
    },
    "Natuurgebied per inwoner": {
        "path": r"Update_Nature_area_per_inhabitant.geojson",
        "year_columns": {
            '2015': 'Year2015',
            '2017': 'Year2017',
        },
        "title": "Natuurgebied per inwoner",
    },
    # Distance to public green areas 
    "Afstand tot openbaar groen": {
        "path": r"DistanceToPublicGreenAreas.geojson",
        "year_columns": {
            '2015': 'Year2015',
            '2017': 'Year2017',
        },
        "title": "Afstand tot openbaar groen",
    },
    "Natuur- en bosgebieden": {
        "path": r"NatureForestAreas.geojson",
        "year_columns": {
            '2015': 'Year2015',
            '2017': 'Year2017',
        },
        "title": "Natuur- en bosgebieden",
    },
    "Broeikasgasemissies per inwoner": {
        "path": r"Update_Greenhouse_gas_emissions.geojson",
        "year_columns": {
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
        },
        "title": "Broeikasgasemissies per inwoner",
    },
    "Kwaliteit van zwemwater binnenwateren": {
        "path": r"QualityOfInlandBathingWater.geojson",
        "year_columns": {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        "title": "Kwaliteit van zwemwater binnenwateren",
    },
    "Kwaliteit van zwemwater kustwateren": {
        "path": r"QualityOfBathingWaterCoastalWaters.geojson",
        "year_columns": {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        "title": "Kwaliteit van zwemwater kustwateren",
    },
    # Average debt per household 
    "Gemiddelde schuld per huishouden": {
        "year_columns": {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        "path": r"AverageDebt.geojson", # check again
        "title": "Gemiddelde schuld per huishouden",
    },
    "Mediaan vermogen van huishoudens": {
        "path": r"MedianHouseholdWealth.geojson",
        "year_columns": {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        "title": "Mediaan vermogen van huishoudens",
    },
    # Private solar energy
    "Particuliere zonne-energie": {
        "path": r"Update_Solar_Energy.geojson", # check again
        "year_columns": {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
        },
        "title": "Particuliere zonne-energie",
    },
    # Built Up area
    "Bebouwd terrein": { 
        "year_columns": {
            '2015': 'Year2015',
            '2017': 'Year2017',
        },
        "path": r"BuiltUpArea.geojson",
        "title": "Bebouwd terrein",
    },
    # Population with a starting qualification 
    "Bevolking met een startkwalificatie": {
        "path": r"PopulationWithStartingQualification.geojson",
        "year_columns": {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2018': 'Year2018',
            '2019': 'Year2019',
            '2020': 'Year2020',
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        "title": "Bevolking met een startkwalificatie",
    },
    "Sociale cohesie": {
        "path": r"SocialCohesion.geojson",
        "year_columns": {
            '2013': 'Year2013',
            '2014': 'Year2014',
            '2015': 'Year2015',
            '2016': 'Year2016',
            '2017': 'Year2017',
            '2019': 'Year2019',
            '2021': 'Year2021',
            '2023': 'Year2023',
        },
        "title": "Sociale cohesie",
    },
    "Geregisteerde problematische schulden": {
        "path": r"RegisteredProblematicDebt.geojson",
        "year_columns": {
            '2021': 'Year2021',
            '2022': 'Year2022',
            '2023': 'Year2023',
        },
        "title": "Geregisteerde problematische schulden",
    },
    "Tevredenheid met sociaal leven": {
        "path": r"SatisfactionWithSocialLife.geojson",
        "year_columns": {
            "2013": "Year2013",
            "2014": "Year2014",
            "2015": "Year2015",
            "2016": "Year2016",
            "2017": "Year2017",
            "2018": "Year2018",
            "2019": "Year2019",
            "2020": "Year2020",
            "2021": "Year2021",
            "2022": "Year2022",
            "2023": "Year2023",
        },
        "title": "Tevredenheid met sociaal leven",
    },
    "Emissions Particulate Matter": {
        "path": r"Update_Emissions_particulate_matter.geojson",
        "year_columns": {
            "2015": "Year2015",
            "2019": "Year2019",
            "2020": "Year2020",
            "2021": "Year2021",
            "2022": "Year2022",
        },
        "title": "Emissions Particulate Matter",
    },
}
    # 40 in total above - in shp folder there is 48 in total including thematic

    file_options_themes = {
    # Thematic
    "Luchtkwaliteit": {
        "path": r"Update_Theme_Air_quality.geojson",
        "year_columns": {
            "2019": "Year2019",
            "2020": "Year2020",
            "2021": "Year2021",
        },
        "title": "Thema Luchtkwaliteit",
    },
    # Wellbeing
    "Subjectief welzijn": { 
        "path": r"ThemeWellbeing.geojson",
        "year_columns": {
            "2013": "Year2013",
            "2014": "Year2014",
            "2015": "Year2015",
            "2016": "Year2016",
            "2017": "Year2017",
            "2018": "Year2018",
            "2019": "Year2019",
            "2020": "Year2020",
            "2021": "Year2021",
            "2022": "Year2022",
        },
        "title": "Thema Subjectief welzijn",
    },
    # Material prosperity
    "Materiale welvaart": { 
        "path": r"ThemeMaterialWellfareandEconomicCapital.geojson",
        "year_columns": {
            "2013": "Year2013",
            "2014": "Year2014",
            "2015": "Year2015",
            "2016": "Year2016",
            "2017": "Year2017",
            "2018": "Year2018",
            "2019": "Year2019",
            "2020": "Year2020",
            "2021": "Year2021",
        },
        "title": "Thema Materiale welvaart",
    },
    "Afstand tot woonvoorzieningen": {
        "path": r"ThemeDistanceToLivingFacilities.geojson",
        "year_columns": {
            "2015": "Year2015",
            "2017": "Year2017",
        },
        "title": "Thema Afstand tot woonvoorzieningen",
    },
    "Milieu": {
        "path": r"Update_Theme_Environment.geojson",
        "year_columns": {
            "2015": "Year2015",
            "2017": "Year2017",
        },
        "title": "Thema Milieu",
    },
    # Health
    "Gezondheid": { 
        "path": r"ThemeHealth.geojson",
        "year_columns": {
            "2016": "Year2016",
            "2020": "Year2020",
            "2022": "Year2022",
        },
        "title": "Thema Gezondheid",
    },

    "Arbeid en vrije tijd": {
        "path": r"ThemeLaborandFreeTime.geojson",
        "year_columns": {
            "2013": "Year2013",
            "2014": "Year2014",
            "2015": "Year2015",
            "2016": "Year2016",
            "2017": "Year2017",
            "2018": "Year2018",
            "2019": "Year2019",
            "2020": "Year2020",
            "2021": "Year2021",
            "2022": "Year2022",
        },
        "title": "Thema Arbeid en Vrije Tijd",
    },
    "Natuurlijk kapitaal": {
        "path": r"Update_Theme_Natural_capital.geojson",
        "year_columns": {
            "2015": "Year2015",
        },
        "title": "Thema Natuurlijk kapitaal",
    },
    "Natuur": {
        "path": r"Update_Theme_Nature.geojson",
        "year_columns": {
            "2015": "Year2015",
            "2017": "Year2017",
        },
        "title": "Thema Natuurlijk kapitaal",
    },
    "Samenleving": {
        "path": r"ThemeSociety.geojson",
        "year_columns": {
            "2013": "Year2013",
            "2014": "Year2014",
            "2015": "Year2015",
            "2016": "Year2016",
            "2017": "Year2017",
            "2018": "Year2018",
            "2019": "Year2019",
            "2020": "Year2020",
            "2021": "Year2021",
            "2022": "Year2022",
        },
        "title": "Thema Samenleving",
    },
}

color_schemes = {
    "Blues": [
        [255, 255, 255],  # White for missing values
        [228, 239, 209],  # 0-25% quantile range
        [152, 197, 194],  # 25-50% quantile range
        [73, 127, 153],   # 50-75% quantile range
        [44, 86, 124]     # 75-100% quantile range
    ],
    "Reds": [
        [255, 255, 255],  # White for missing values
        [255, 194, 179],  # 0-25% quantile range
        [255, 112, 77],   # 25-50% quantile range
        [230, 46, 0],     # 50-75% quantile range
        [153, 31, 0]      # 75-100% quantile range
    ],
    "Purples": [
        [255, 255, 255],  # White for missing values
        [255, 204, 255],  # 0-25% quantile range
        [255, 128, 255],  # 25-50% quantile range
        [255, 51, 255],   # 50-75% quantile range
        [204, 0, 204]     # 75-100% quantile range
    ],
    "Greens": [
        [255, 255, 255],  # White for missing values
        [204, 255, 204],  # 0-25% quantile range
        [128, 255, 128],  # 25-50% quantile range
        [51, 255, 51],    # 50-75% quantile range
        [0, 230, 0],      # 75-100% quantile range
        [0, 153, 0]       # 75-100% quantile range
    ]
}
