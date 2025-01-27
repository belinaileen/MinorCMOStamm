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
file_options = {
    "Mediaan besteedbaar inkomen": {
        "year_columns": {
            "2013": "F_01K_Mean",
            "2014": "F_011_Mean",
            "2015": "F_012_Mean",
            "2016": "F_013_Mean",
            "2017": "F_014_Mean",
            "2018": "F_015_Mean",
            "2019": "F_016_Mean",
            "2020": "F_017_Mean",
            "2021": "F_018_Mean",
        },
        "path": 'MedianDisposableIncome.geojson',
        "title": "Mediaan besteedbaar inkomen",
    },
    "Tevredenheid met het leven": {
        "path": r"SatisfactionLife.geojson",
        "year_columns": {
            "2013": "F_01K_Mean",
            "2014": "F_011_Mean",
            "2015": "F_012_Mean",
            "2016": "F_013_Mean",
            "2017": "F_014_Mean",
            "2018": "F_015_Mean",
            "2019": "F_016_Mean",
            "2020": "F_017_Mean",
            "2021": "F_018_Mean",
            "2022": "F_01K_Me_1",
        },
        "title": "Tevredenheid met het leven",
    },
    "Tevredenheid met vrije tijd": {
        "path": r"SatisfactionFreeTime.geojson",
        "year_columns": {
            "2013": "F_01K_Mean",
            "2014": "F_011_Mean",
            "2015": "F_012_Mean",
            "2016": "F_013_Mean",
            "2017": "F_014_Mean",
            "2018": "F_015_Mean",
            "2019": "F_016_Mean",
            "2020": "F_017_Mean",
            "2021": "F_018_Mean",
            "2022": "F_01K_Me_1",
        },
        "title": "Tevredenheid met vrije tijd",
    },  
    "Overgewicht": {
        "path": r"Overweight.geojson",
        "year_columns": {
            "2016": "F_01G_Mean",
            "2020": "F_011_Mean",
            "2022": "F_012_Mean",
        },
        "title": "Overgewicht",
    },
    "Ervaren gezondheid": {
        "path": r"ExperiencedHealth.geojson",
        "year_columns": {
            "2016": "F_01K_Mean",
            "2020": "F_011_Mean",
            "2022": "F_012_Mean",
        },
        "title": "Ervaren gezondheid",
    },
    "Levensverwachting bevolking": {
        "path": r"LifeExpectancyOfThePopulation.geojson",
        "year_columns": {
            "2021": "F_01G_Mean",
        },
        "title": "Levensverwachting bevolking",
    },
    "Personen met één of meer langdurige ziekten of aandoeningen": {
        "path": r"PeopleWithIllness.geojson",
        "year_columns": {
            "2016": "F_RGZ_Mean",
            "2020": "F_RG1_Mean",
            "2022": "F_RG2_Mean",
        },
        "title": "Personen met één of meer langdurige ziekten of aandoeningen",
    },
    "Nettoarbeidsparticipatie": {
        "path": r"NetLaborParticipation.geojson",
        "year_columns": {
            "2014": "mean14",
            "2015": "mean15",
            "2016": "mean16",
            "2017": "mean17",
            "2018": "mean18",
            "2019": "mean19",
            "2020": "mean20",
            "2021": "mean21",
            "2022": "mean22",

        },
        "title": "Nettoarbeidsparticipatie",
    },
    "Werkloosheid": {
        "year_columns": {
            "2014": "mean14",
            "2015": "mean15",
            "2016": "mean16",
            "2017": "mean17",
            "2018": "mean18",
            "2019": "mean19",
            "2020": "mean20",
            "2021": "mean21",
            "2022": "mean22",
        },
        "path": r"Unemployment.geojson",
        "title": "Werkloosheid",
    },
    # Distance to public transport - move to GitHub
    "Afstand tot ov": {
        "path": r"DistanceToPublicTransportation.geojson",
        "year_columns": {
            "2017": "spill17",
            "2018": "spill18",
            "2019": "spill19",
            "2020": "spill20",
            "2021": "spill21",
            "2022": "spill22",
        },
        "title": "Afstand tot ov",
    },
    "Tevredenheid met woonomgeving": {
        "path": r"SatisfactionLivingEnvironment.geojson",
        "year_columns": {
            "2015": "F_03P_Mean",
            "2018": "F_031_Mean",
            "2021": "F_032_Mean",
        },
        "title": "Tevredenheid met woonomgeving",
    },
    "Tevredenheid met woning": {
        "year_columns": {
            "2015": "F_01K_Mean",
            "2018": "F_011_Mean",
            "2021": "F_012_Mean",
        },
        "path": r"SatisfactionHousing.geojson",
        "title": "Tevredenheid met woning",
    },
    "Afstand tot sportterrein": {
        "path": r"DistanceToSportsField.geojson",
        "year_columns": {
            "2015": "spill15",
            "2017": "spill17",
        },
        "title": "Afstand tot sportterrein",
    },
    # Distance to Primary school - move to GitHub
    "Afstand tot basisschool": {
        "path": r"DistanceToPrimarySchool.geojson",
        "year_columns": {
            "2013": "spill13",
            "2014": "spill14",
            "2015": "spill15",
            "2016": "spill16",
            "2017": "spill17",
            "2018": "spill18",
            "2019": "spill19",
            "2020": "spill20",
            "2021": "spill21",
            "2022": "spill22",
        },
        "title": "Afstand tot basisschool",
    },
    # Distance to cafe - move to GitHub
    "Afstand tot café e.d.": {
        "path": r"DistanceToCafe.geojson",
        "year_columns": {
            "2013": "spill13",
            "2014": "spill14",
            "2015": "spill15",
            "2016": "spill16",
            "2017": "spill17",
            "2018": "spill18",
            "2019": "spill19",
            "2020": "spill20",
            "2021": "spill21",
            "2022": "spil22",
        },
        "title": "Afstand tot café e.d.",
    },
    # Contact with family, friends or neighbors - move to GitHub
    "Contact met familie, vrienden of buren": {
        "path": r"ContactWithFamilyEtc.geojson",
        "year_columns": {
            "2013": "F_01K_Mean",
             "2014": "F_011_Mean",
             "2015": "F_012_Mean",
             "2016": "F_013_Mean",
             "2017": "F_014_Mean",
             "2018": "F_015_Mean",
             "2019": "F_016_Mean",
             "2020": "F_017_Mean",
             "2021": "F_018_Mean",
             "2022": "F_01K_Me_2",
        },
        "title": "Contact met familie, vrienden of buren",
    },
    "Vertrouwen in instituties": {
        "path": r"TrustInstitutions.geojson",
        "year_columns": {
            "2013": "mean13",
            "2014": "mean14",
            "2015": "mean15",
            "2016": "mean16",
            "2017": "mean17",
            "2018": "mean18",
            "2019": "mean19",
            "2020": "mean20",
            "2021": "mean21",
            "2022": "mean22_1",
        },
        "title": "Vertrouwen in instituties",
    },
    "Vertrouwen in anderen": {
        "path": r"TrustOthers.geojson",
        "year_columns": {
            "2013": "mean13",
            "2014": "mean14",
            "2015": "mean15",
            "2016": "mean16",
            "2017": "mean17",
            "2018": "mean18",
            "2019": "mean19",
            "2020": "mean20",
            "2021": "mean21_1",
            "2022": "mean22_1",
        },
    },
        "title": "Vertrouwen in anderen",
    "Vrijwilligerswerk": {
        "year_columns": {
            "2013": "F_01K_Mean",
            "2014": "F_011_Mean",
            "2015": "F_012_Mean",
            "2016": "F_013_Mean",
            "2017": "F_014_Mean",
            "2018": "F_015_Mean",
            "2019": "F_016_Mean",
            "2020": "F_017_Mean",
            "2021": "F_01K_Me_1",
            "2022": "F_01K_Me_2",
        },
        "path": r"VolunteerWork.geojson",
        "title": "Vrijwilligerswerk",
    },
    # often feeling unsafe in neighborhood
    "Vaak onveilig gevoel in de buurt": {
        "path": r"OftenFeelingUnsafe.geojson",
        "year_columns": {
            "2013": "F_01K_Mean",
            "2014": "F_01K_Me_1",
            "2015": "F_01K_Me_2",
            "2016": "F_01K_Me_3",
            "2017": "F_01K_Me_4",
            "2019": "F_01K_Me_5",
            "2021": "F_01K_Me_6",
        },
        "title": "Vaak onveilig gevoel in de buurt",
    },
    "Aantal ondervonden delicten": {
        "path": r"Update_Number_crimes_encountered.geojson",
        "year_columns": {
            "2013": "F_RHN_Mean",
            "2014": "F_RH1_Mean",
            "2015": "F_RHN_Me_1",
            "2016": "F_RHN_Me_2",
            "2017": "F_RHN_Me_3",
            "2019": "F_RHN_Me_4",
            "2021": "F_RHN_Me_5",
        },
        "title": "Aantal ondervonden delicten",
    },
    "Geregistreerde misdrijven": {
        "year_columns": {
            "2013": "F_04V_Mean",
            "2014": "F_04V_Me_1",
            "2015": "F_04V_Me_2",
            "2016": "F_041_Mean",
            "2017": "F_042_Me_1",
            "2018": "F_043_Me_1",
            "2019": "F_044_Me_1",
            "2020": "F_045_Me_1",
            "2021": "F_046_Me_1",
            "2022": "F_047_Me_1",
        },
        "path": r"Update_Recorded_crimes.geojson",
        "title": "Geregistreerde misdrijven",
    },
    "Natuurgebied per inwoner": {
        "path": r"Update_Nature_area_per_inhabitant.geojson",
        "year_columns": {
            "2015": "Mean_15",
            "2017": "Mean_17",
        },
        "title": "Natuurgebied per inwoner",
    },
    # Distance to public green areas - move to GitHub
    "Afstand tot openbaar groen": {
        "path": r"DistanceToPublicGreenAreas.geojson",
        "year_columns": {
            "2015": "spill15",
            "2017": "spill17",
        },
        "title": "Afstand tot openbaar groen",
    },
    "Natuur- en bosgebieden": {
        "path": r"NatureForestAreas.geojson",
        "year_columns": {
            "2015": "spill15",
            "2017": "spill17",
        },
        "title": "Natuur- en bosgebieden",
    },
    "Broeikasgasemissies per inwoner": {
        "path": r"Update_Greenhouse_gas_emissions.geojson",
        "year_columns": {
            "2015": "F_07KE015",
            "2016": "F_07KE016",
            "2017": "F_07KE017",
            "2018": "F_07KE018",
            "2019": "F_07KE019",
            "2020": "F_07KE020",
            "2021": "F_07KE021",
        },
        "title": "Broeikasgasemissies per inwoner",
    },
    "Kwaliteit van zwemwater binnenwateren": {
        "path": r"QualityOfInlandBathingWater.geojson",
        "year_columns": {
            "2013": "mean13",
            "2014": "mean14_1",
            "2015": "mean15_1",
            "2016": "mean16_1",
            "2017": "mean17_1",
            "2018": "mean18_1",
            "2019": "mean19_1",
            "2020": "mean20_1",
            "2021": "mean21_1",
            "2022": "mean22_1",
        },
        "title": "Kwaliteit van zwemwater binnenwateren",
    },
    "Kwaliteit van zwemwater kustwateren": {
        "path": r"QualityOfBathingWaterCoastalWaters.geojson",
        "year_columns": {
            "2013": "mean13",
            "2014": "mean14",
            "2015": "mean15",
            "2016": "mean16",
            "2017": "mean17",
            "2018": "mean18",
            "2019": "mean19",
            "2020": "mean20",
            "2021": "mean21",
            "2022": "mean22",
        },
        "title": "Kwaliteit van zwemwater kustwateren",
    },
    # Average debt per household 
    "Gemiddelde schuld per huishouden": {
        "year_columns": {
            "2013": "F_18F_Me_1",
            "2014": "F_181_Me_1",
            "2015": "F_182_Me_1",
            "2016": "F_183_Me_1",
            "2017": "F_184_Me_1",
            "2018": "F_185_Me_1",
            "2019": "F_186_Me_1",
            "2020": "F_187_Me_1",
            "2021": "F_188_Me_1",
            "2022": "F_189_Me_1",
        },
        "path": r"AverageDebt.geojson", # check again
        "title": "Gemiddelde schuld per huishouden",
    },
    "Mediaan vermogen van huishoudens": {
        "path": r"MedianHouseholdWealth.geojson",
        "year_columns": {
            "2013": "F_010_Mean",
            "2014": "F_011_Mean",
            "2015": "F_012_Mean",
            "2016": "F_013_Mean",
            "2017": "F_014_Mean",
            "2018": "F_015_Mean",
            "2019": "F_016_Mean",
            "2020": "F_017_Mean",
            "2021": "F_018_Mean",
        },
        "title": "Mediaan vermogen van huishoudens",
    },
    # Private solar energy
    "Particuliere zonne-energie": {
        "path": r"Update_Solar_Energy.geojson", # check again
        "year_columns": {
        "2013": "mean13",
        "2014": "mean14_1",
        "2015": "mean15_1",
        "2016": "mean16_1",
        "2017": "mean17",
        "2018": "mean18",
        "2019": "mean19",
        "2020": "mean20",
        "2021": "mean21",
        "2022": "mean22",
        },
        "title": "Particuliere zonne-energie",
    },
    # Built Up area
    "Bebouwd terrein": { 
        "year_columns": {
        "2015": "F_RLN_Mean",
        "2017": "F_RL1_Mean",
        },
        "path": r"BuiltUpArea.geojson",
        "title": "Bebouwd terrein",
    },
    # Population with a starting qualification 
    "Bevolking met een startkwalificatie": {
        "path": r"PopulationWithStartingQualification.geojson",
        "year_columns": {
            "2013": "mean13",
            "2014": "mean14",
            "2015": "mean15",
            "2016": "mean16",
            "2017": "mean17",
            "2018": "mean18",
            "2019": "mean19",
            "2020": "mean20",
            "2021": "mean21",
            "2022": "mean22",
        },
        "title": "Bevolking met een startkwalificatie",
    },
    "Sociale cohesie": {
        "path": r"SocialCohesion.geojson",
        "year_columns": {
            "2013": "F_RLS_Me_1",
            "2014": "F_RLS_Me_2",
            "2015": "F_RL1_Me_3",
            "2016": "F_RL2_Me_4",
            "2017": "F_RL3_Me_5",
            "2019": "F_RL4_Me_6",
            "2021": "F_RL5_Me_7",
        },
        "title": "Sociale cohesie",
    },
    "Geregisteerde problematische schulden": {
        "path": r"RegisteredProblematicDebt.geojson",
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

# Indicator 01.10_NW has been added. Registered problematic debt /
# Geregisteerde problematische schulden
# Indicator 10.31_NW has been added. Satisfaction with social life / 
# Tevredenheid met sociaal leven

    # 40 in total above - in shp folder there is 48 in total including thematic
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
