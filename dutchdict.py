# Define the themes and their corresponding markdown content
import streamlit as st

Themes = {
        "Tevredenheid met het leven": """
        **Welkom bij Tevredenheid met het leven indicator**
        - Deze indicator is onderdeel van het Subjectief welzijn thema.
        - Voorlopige cijfers. Bij het toevoegen van een nieuw jaar schat 
        het model alle jaren uit de reeks opnieuw. Raadpleeg de Technische 
        Toelichting voor meer uitleg over de interpretatie van de modelschattingen 
        en de marges.
        - Meeteenheid: Percentage Nederlanders geeft het leven een 7 of hoger
    """,
    "Tevredenheid met vrije tijd": """
        **Welkom bij Tevredenheid met vrije tijd indicator**
        - Deze indicator is onderdeel van het Subjectief welzijn thema.
        - Voorlopige cijfers. Bij het toevoegen van een nieuw jaar schat het 
        model alle jaren uit de reeks opnieuw. Raadpleeg de Technische Toelichting 
        voor meer uitleg over de interpretatie van de modelschattingen en de marges.
        - Meeteenheid: Percentage van de bevolking van 18+ is (zeer) tevreden
    """,
    "Mediaan besteedbaar inkomen": """
        **Welkom bij Mediaan besteedbaar inkomen indicator**
        - Deze indicator is onderdeel van het Materiële welvaart
        - 2021 zijn voorlopige cijfers en de correctie voor de prijsverandering 
        in 2021 is gebaseerd op de onderzoeksreeks consumentenprijzen, die de daadwerkelijk 
        betaalde energieprijzen gebruikt. Deze sluit gemiddeld genomen meer aan bij de 
        prijsontwikkeling die de bevolking heeft ervaren dan de consumentenprijsindex.
        - Meeteenheid: Euro per huishouden in constante prijzen in 2021
    """,
    "Bruto binnenlands product": """
        **Welkom bij Bruto binnenlands product indicator**
        - Deze indicator is onderdeel van het Materiële welvaart thema.
        - 2022 cijfers zijn voorlopig
        - Meeteenheid: Euro per inwoner in prijzen van 2015
    """,
    "Overgewicht": """
        **Welkom bij Overgewicht indicator**
        - Deze indicator is onderdeel van het Gezondheid thema.
        - Voor de jaren 2012 en 2016 is de gemeten populatie 19+
        - Meeteenheid: percentage van de bevolking van 18 jaar en ouder is te zwaar
    """,
    "Ervaren gezondheid": """
        **Welkom bij Ervaren gezondheid indicator**
        - Deze indicator is onderdeel van het Gezondheid thema.
        - Voor de jaren 2012 en 2016 is de gemeten populatie 19+
        - Meeteenheid: percentage van de bevolking van 18 jaar en ouder beschouwt zijn/haar eigen gezondheid als (zeer) goed
    """,
    "Levensverwachting bevolking": """
        **Welkom bij Levensverwachting bevolking indicator**
        - Deze indicator is onderdeel van het Gezondheid thema.
        - Gemiddelde levensverwachting over periode 2018-2021, niet apart per jaar bepaald
        - Meeteenheid: levensverwachting in jaren bij geboorte
    """,
    "Personen met één of meer langdurige ziekten of aandoeningen": """
        **Welkom bij Personen met één of meer langdurige ziekten of aandoeningen indicator**
        - Deze indicator is onderdeel van het Gezondheid thema.
        - Voor de jaren 2012 en 2016 is de gemeten populaite 19+
        - Meeteenheid: percentage van de bevolking van 18 jaar of ouder
    """,
    "Nettoarbeidsparticipatie": """
        **Welkom bij Nettoarbeidsparticipatie indicator**
        - Deze indicator is onderdeel van het Arbeid en vrije tijd thema.
        - Meeteenheid: percentage van de bevolking van 15 tot 74 jaar
    """,
    "Brutoarbeidsparticipatie": """
        **Welkom bij Brutoarbeidsparticipatie indicator**
        - Deze indicator is onderdeel van het Arbeid en vrije tijd thema.
        - Meeteenheid: percentage van de bevolking van 15 tot 74 jaar
    """,
    "Hoogopgeleide bevolking": """
        **Welkom bij Hoogopgeleide bevolking indicator**
        - Deze indicator is onderdeel van het Arbeid en vrije tijd thema.
        - Meeteenheid: percentage van de bevolking (15 tot 74 jaar) dat hoger onderwijs heeft afgerond
    """,
    "Werkloosheid": """
        **Welkom bij Werkloosheid indicator**
        - Deze indicator is onderdeel van het Arbeid en vrije tijd thema.
        - Meeteenheid: percentage van de beroepsbevolking
    """,
    "Vacaturegraad": """
        **Welkom bij Vacaturegraad indicator**
        - Deze indicator is onderdeel van het Arbeid en vrije tijd thema.
        - 2021 en 2022 zijn voorlopige cijfers
        - Meeteenheid: aantal vacatures per 1.000 banen
    """,
    "Afstand tot ov": """
        **Welkom bij Afstand tot ov indicator**
        - Deze indicator is onderdeel van het Arbeid en vrije tijd thema.
        - Meeteenheid: kilometers
    """,
    "Tevredenheid met woonomgeving": """
        **Welkom bij Tevredenheid met woonomgeving indicator**
        - Deze indicator is onderdeel van het Wonen thema.
        - Meeteenheid: percentage particuliere huishoudens dat (zeer) tevreden is
    """,
    "Tevredenheid met woning": """
        **Welkom bij Tevredenheid met woning indicator**
        - Deze indicator is onderdeel van het Wonen thema.
        - Meeteenheid: percentage particuliere huishoudens dat (zeer) tevreden is
    """,
    "Afstand tot sportterrein": """
        **Welkom bij Afstand tot sportterrein indicator**
        - Deze indicator is onderdeel van het Wonen thema.
        - Meeteenheid: kilometers
    """,
    "Afstand tot basisschool": """
        **Welkom bij Afstand tot basisschool indicator**
        - Deze indicator is onderdeel van het Wonen thema.
        - Meeteenheid: kilometers
    """,
    "Afstand tot café e.d.": """
        **Welkom bij Afstand tot café e.d. indicator**
        - Deze indicator is onderdeel van het Wonen thema.
        - Meeteenheid: kilometers
    """,
    "Contact met familie, vrienden of buren": """
        **Welkom bij Contact met familie, vrienden of buren indicator**
        - Deze indicator is onderdeel van het Samenleving thema.
        - Voorlopige cijfers. Bij het toevoegen van een nieuw jaar schat het model alle jaren uit de reeks opnieuw. Raadpleeg de Technische Toelichting voor meer uitleg over de interpretatie van de modelschattingen en de marges.
        - Meeteenheid: percentage van de bevolking van 15+ dat gemiddeld minstens één keer per week met iemand in contact komt
    """,
    "Vertrouwen in instituties": """
        **Welkom bij Vertrouwen in instituties indicator**
        - Deze indicator is onderdeel van het Samenleving thema.
        - Voorlopige cijfers. Bij het toevoegen van een nieuw jaar schat het model alle jaren uit de reeks opnieuw. Raadpleeg de Technische Toelichting voor meer uitleg over de interpretatie van de modelschattingen en de marges.
        - Meeteenheid: percentage van de bevolking van 15+ heeft voldoende vertrouwen
    """,
    "Vertrouwen in anderen": """
        **Welkom bij Vertrouwen in anderen indicator**
        -Deze indicator is onderdeel van het Samenleving thema.
        -Voorlopige cijfers. Bij het toevoegen van een nieuw jaar schat het model alle jaren uit de reeks opnieuw. Raadpleeg de Technische Toelichging voor meer uitleg over de interpretatie van de modelschattingen en de marges.
        - Meeteenheid: percentage van de bevolking van 15+ vindt de meeste mensen betrouwbaar
    """,
    "Vrijwilligerswerk": """
        **Welkom bij Vrijwilligerswerk indicator**
        - Deze indicator is onderdeel van het Samenleving thema.
        - Voorlopige cijfers. Bij het toevoegen van een nieuw jaar schat het model alle jaren uit de reeks opnieuw. Raadpleeg de Technische Toelichging voor meer uitleg over de interpretatie van de modelschattingen en de marges.
        - Meeteenheid: percentage van de bevolking van 15 jaar en ouder dat georganiseerd vrijwilligerswerk doet
    """,
    "Vaak onveilig voelen in de buurt": """
        **Welkom bij Vaak onveilig voelen in de buurt indicator**
        - Deze indicator is onderdeel van het Veiligheid thema.
        - Meeteenheid: percentage van de bevolking van 15 jaar en ouder
    """,
    "Aantal ondervonden delicten": """
        **Welkom bij Aantal ondervonden delicten indicator**
        - Deze indicator is onderdeel van het Veiligheid thema.
        - Meeteenheid: aantal misdrijven per 100 inwoners
    """,
    "Geregistreerde misdrijven": """
        **Welkom bij Geregistreerde misdrijven indicator**
        - Deze indicator is onderdeel van het Veiligheid thema.
        - 2021 en 2022 zijn voorlopige cijfers
        - Meeteenheid: geregistreerde misdaden per 1000 inwoners
    """,
    "Natuurgebied per inwoner": """
        **Welkom bij Natuurgebied per inwoner indicator**
        - Deze indicator is onderdeel van het Milieu thema
        - Meeteenheid: ha per 1000 inwoners
    """,
    "Emissies van fijnstof naar lucht": """
        **Welkom bij Emissies van fijnstof naar lucht indicator**
        - Deze indicator is onderdeel van het Milieu thema
        - Meeteenheid: microgram PM 2,5 per m^3
    """,
    "Afstand tot openbaar groen": """
        **Welkom bij Afstand tot openbaar groen indicator**
        - Deze indicator is onderdeel van het Milieu thema
        - Meeteenheid: Kilometers
    """,
    "Natuur- en bosgebieden": """
        **Welkom bij Natuur- en bosgebieden indicator**
        - Deze indicator is onderdeel van het Milieu thema
        - Meeteenheid: Percentage van het landoppervlak
    """,
    "Broeikasgasemissies per inwoner": """
        **Welkom bij Broeikasgasemissies per inwoner indicator**
        - Deze indicator is onderdeel van het Milieu thema
        - De gehele reeks is aangepast vanwege de nieuwe IPCC voorschriften.
        - Meeteenheid: Tonnen CO2-equivalent per inwoner
    """,
    "Kwaliteit van zwemwater binnenwateren": """
        **Welkom bij Kwaliteit van zwemwater binnenwateren indicator**
        - Deze indicator is onderdeel van het Milieu thema
        - Meeteenheid: Gemiddelde kwaliteit (1=slecht tot 4=uitstekend)
    """,
    "Kwaliteit van zwemwater kustwateren": """
        **Welkom bij Kwaliteit van zwemwater kustwateren indicator**
        - Deze indicator is onderdeel van het Milieu thema
        - Meeteenheid: Gemiddelde kwaliteit (1=slecht tot 4=uitstekend)
    """,
    "Gemiddelde schuld per huishouden": """
        **Welkom bij Gemiddelde schuld per huishouden indicator**
        - Deze indicator is onderdeel van het Economisch kapitaal
        - 2022 zijn voorlopige cijfers en de correctie voor de prijsverandering in 2021 en 2022 is gebaseerd op de onderzoeksreeks consumentenprijzen, die de daadwerkelijk betaalde energieprijzen gebruikt. Deze sluit gemiddeld genomen meer aan bij de prijsontwikkeling die de bevolking heeft ervaren dan de consumentenprijsindex.
        - Meeteenheid: Gemiddelde schuld per huishouden in euro
    """,
    "Mediaan vermogen van huishoudens": """
        **Welkom bij Mediaan vermogen van huishoudens indicator**
        - Deze indicator is onderdeel van het Economisch kapitaal
        - 2021 zijn voorlopige cijfers en de correctie voor de prijsverandering in 2021 is gebaseerd op de onderzoeksreeks consumentenprijzen, die de daadwerkelijk betaalde energieprijzen gebruikt. Deze sluit gemiddeld genomen meer aan bij de prijsontwikkeling die de bevolking heeft ervaren dan de consumentenprijsindex.
        - Meeteenheid: Euro
    """,
    "Particuliere zonne-energie": """
        **Welkom bij Particuliere zonne-energie indicator**
        - Deze indicator is onderdeel van het Natuurlijk kapitaal
        - cijfers 2021 en 2022 zijn voorlopig
        - Meeteenheid: Watt per huis
    """,
    "Natuur- en bosgebieden": """
        **Welkom bij Natuur- en bosgebieden indicator**
        - Deze indicator is onderdeel van het Natuurlijk kapitaal
        - Meeteenheid: Percentage van het landoppervlak
    """,
    "Bebouwd terrein": """
        **Welkom bij Bebouwd terrein indicator**
        - Deze indicator is onderdeel van het Natuurlijk kapitaal
        - Meeteenheid: Percentage van het landoppervlak
    """,
    "Fosfaatuitscheiding landbouw": """
        **Welkom bij Fosfaatuitscheiding landbouw indicator**
        - Deze indicator is onderdeel van het Natuurlijk kapitaal
        - Meeteenheid: kg per ha bemest landbouwgrond
    """,
    "Groen-blauwe ruimte, exclusief reguliere landbouw": """
        **Welkom bij Groen-blauwe ruimte, exclusief reguliere landbouw indicator**
        - Deze indicator is onderdeel van het Natuurlijk kapitaal
        - Meeteenheid: m^2 green and freshwater area per inhabitant
    """,
    "Stikstofuitscheiding landbouw": """
        **Welkom bij Stikstofuitscheiding landbouw indicator**
        - Deze indicator is onderdeel van het Natuurlijk kapitaal
        - Meeteenheid: kg per ha bemest landbouwgrond
    """,
    "Arbeidsduur per week": """
        **Welkom bij Arbeidsduur per week indicator**
        - Deze indicator is onderdeel van het Menselijk kapitaal
        - 2021 en 2022 zijn voorlopige cijfers
        - Meeteenheid: uur aantal uren dat daadwerkelijk per werknemer per week wordt gewerkt
    """,
    "Hoogopgeleide bevolking": """
        **Welkom bij Hoogopgeleide bevolking indicator**
        - Deze indicator is onderdeel van het Menselijk kapitaal
        - Meeteenheid: Percentage van de bevolking (15 tot 74 jaar) dat hoger onderwijs heeft afgerond
    """,
    "Ervaren gezondheid": """
        **Welkom bij Ervaren gezondheid indicator**
        - Deze indicator is onderdeel van het Menselijk kapitaal
        - Voor de jaren 2012 en 2016 is de gemeten populatie 19+
        - Meeteenheid: percentage van de bevolking van 18 jaar en ouder beschouwt zijn/haar eigen gezondheid als (zeer) goed
    """,
    "Sociale cohesie": """
        **Welkom bij Sociale cohesie indicator**
        - Deze indicator is onderdeel van het Sociaal kapitaal
        - Meeteenheid: schaalscore (0-10)
    """,

    # Themes 

    "Gezondheid": """
        **Welkom bij het thema Gezondheid**
        - In dit thema zijn de volgende indicatoren opgenomen: Overgewicht, Ervaren gezondheid, Levensverwachting van de bevolking, Mensen met een of meer langdurige ziekten of aandoeningen
    """,
    "Subjectief welzijn": """
        **Welkom bij het thema Welzijn**
        - In dit thema zijn de volgende indicatoren opgenomen: Tevredenheid met het leven, Tevredenheid met vrije tijd
    """,
    "Materiale welvaart": """
        **Welkom bij het thema Materieel Welzijn en Economisch Kapitaal**
        - In dit thema zijn de volgende indicatoren opgenomen: Mediaan besteedbaar inkomen, Bruto binnenlands product, Gemiddelde schuld per huishouden, Mediaan huishoudvermogen
    """,
    "Arbeid en vrije tijd": """
        **Welkom bij het thema Arbeid en Vrije Tijd**
        - In dit thema zijn de volgende indicatoren opgenomen: Netto arbeidsparticipatie, Bruto arbeidsparticipatie, Hoogopgeleide bevolking, Werkloosheid, Vacaturepercentage
    """,
    # ??
    "Levend": """
        **Welkom bij het thema Leven**
        - In dit thema zijn de volgende indicatoren opgenomen: Tevredenheid met de leefomgeving, Tevredenheid met de huisvesting, Afstand tot sportveld, Afstand tot basisschool, Afstand tot café, Vertrouwen in instellingen, Vertrouwen in anderen, Vrijwilligerswerk
    """,
    # ?? 
    "Veiligheid": """
        **Welcome to the Safety theme**
        - In dit thema zijn de volgende indicatoren opgenomen: Vaak onveilig gevoel in de buurt, Aantal aangetroffen misdrijven, Geregistreerde misdrijven
    """,
    "Milieu": """
        **Welkom bij het thema Milieu**
        - In dit thema zijn de volgende indicatoren opgenomen: Oppervlakte natuurgebied per inwoner, Emissies van fijnstof naar de lucht, Natuur- en bosgebieden, Afstand tot openbaar groen, Uitstoot broeikasgassen per hoofd van de bevolking, Kwaliteit zwemwater in het binnenland, Kwaliteit zwemwater aan de kust
    """,
    "Luchtkwaliteit": """
        **Welkom bij het thema Luchtkwaliteit**
        - In dit thema zijn de volgende indicatoren opgenomen: Emissies van fijnstof naar de lucht, Broeikasgasemissies per hoofd van de bevolking
    """,
    "Natuurlijk kapitaal": """
        **Welkom bij het thema Natuurlijk Kapitaal**
        - In dit thema zijn de volgende indicatoren opgenomen: Particuliere zonne-energie, Natuur- en bosgebieden, Gebouwde omgeving, Emissies van fijnstof, Groenblauwe infrastructuur
    """,
    "Natuur":"""
        **Welkom bij het thema Natuur**
        - In dit thema zijn de volgende indicatoren opgenomen: ....
    """,
    "Afstand tot woonvoorzieningen":"""
        **Welkom bij het thema Afstand tot Woonvoorzieningen**
        - In dit thema zijn de volgende indicatoren opgenomen: ....
    """,
}