# Define the themes and their corresponding markdown content
import streamlit as st

Themes = {
        "Tevredenheid met het leven": """
        **Welkom bij Tevredenheid met het leven indicator**
        - Deze indicator is onderdeel van het Subjectief welzijn thema.
        - Voorlopige cijfers. Bij het toevoegen van een nieuw jaar schat het model alle jaren uit de reeks opnieuw. Raadpleeg de Technische Toelichting voor meer uitleg over de interpretatie van de modelschattingen en de marges.
        - Meeteenheid: Percentage Nederlanders geeft het leven een 7 of hoger
        - Voor deze indicator kan geen specifieke ruimtelijke spillover-/compensatieafstand worden aangenomen, omdat hierover geen relevante literatuur beschikbaar is. Daarom wordt in deze analyse een eerste-orde-contiguïteit (first order contiguity) toegepast. Dit betekent dat aangenomen wordt dat wanneer gemeenten een grens delen, tevredenheid met het leven over deze grenzen heen overloopt. De gemiddelde waarde voor tevredenheid met het leven per gemeente wordt gegeven door het CBS, als percentage van de bevolking van 18 jaar en ouder die tevreden is met het leven.
        - Om rekening te houden met de bevolkingsgrootte van elke gemeente, moest het percentage van de inwoners van 18 jaar en ouder die tevreden zijn met het leven worden omgezet naar het totale aantal inwoners (18+) die tevreden zijn. Aangezien de CBS-gegevens zijn gegevens voor inwoners van 18 jaar en ouder, maar er geen gegevens zijn over het aantal inwoners in deze leeftijdsgroep, is de bevolking van 15 jaar en ouder gebruikt in de verdere berekeningen. De resultaten van de verdere berekeningen zullen waarschijnlijk verschillen van de resultaten als gegevens over de leeftijdsgroep van 18 jaar en ouder beschikbaar zouden zijn geweest.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over tevredenheid met het leven geanalyseerd met behulp van ArcGIS Pro. Eerst werden aangrenzende gemeenten bepaald op basis van gedeelde grenzen, gedefinieerd als geometrieën die elkaar raken. Vervolgens werden voor elke gemeente twee variabelen geactiveerd: één om de bevolking van de gemeente en haar aangrenzende gemeenten die tevreden zijn met het leven op te tellen, en een andere om de totale bevolking van de gemeente en haar aangrenzende gemeenten op te tellen. Het doel is om een gecombineerde tevredenheidsscore te berekenen door ook de aangrenzende gemeenten mee te nemen.
        - Het berekende totale aantal tevreden inwoners en het totale aantal inwoners werden vervolgens gebruikt om terug te rekenen naar het percentage tevreden inwoners.
    """,
    "Tevredenheid met vrije tijd": """
        **Welkom bij Tevredenheid met vrije tijd indicator**
        - Deze indicator is onderdeel van het Subjectief welzijn thema.
        - Voorlopige cijfers. Bij het toevoegen van een nieuw jaar schat het 
        model alle jaren uit de reeks opnieuw. Raadpleeg de Technische Toelichting 
        voor meer uitleg over de interpretatie van de modelschattingen en de marges.
        - Meeteenheid: Percentage van de bevolking van 18+ is (zeer) tevreden
        - Voor deze indicator kan geen specifieke ruimtelijke spillover-/compensatieafstand worden aangenomen, omdat hierover geen relevante literatuur beschikbaar is. Daarom wordt in deze analyse een eerste-orde-contiguïteit (first order contiguity) toegepast. Dit betekent dat aangenomen wordt dat wanneer gemeenten een grens delen, tevredenheid met vrije tijd over deze grenzen heen overloopt. De gemiddelde waarde voor tevredenheid met vrije tijd per gemeente wordt gegeven door het CBS, als percentage van de bevolking van 18 jaar en ouder die tevreden is met hun vrije tijd.
        - Om rekening te houden met de bevolkingsgrootte van elke gemeente, moest het percentage van de inwoners van 18 jaar en ouder die tevreden zijn met hun vrije tijd worden omgezet naar het totale aantal inwoners (18+) die tevreden zijn. Aangezien de CBS-gegevens zijn verstrekt voor inwoners van 18 jaar en ouder, maar er geen gegevens zijn over het aantal inwoners in deze leeftijdsgroep, is de bevolking van 15 jaar en ouder gebruikt in de verdere berekeningen. De resultaten van de verdere berekeningen zullen waarschijnlijk verschillen van de resultaten als gegevens over de leeftijdsgroep van 18 jaar en ouder beschikbaar zouden zijn geweest.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over tevredenheid met vrije tijd geanalyseerd met behulp van ArcGIS Pro. Eerst werden aangrenzende gemeenten bepaald op basis van gedeelde grenzen, gedefinieerd als geometrieën die elkaar raken. Vervolgens werden voor elke gemeente twee variabelen geactiveerd: één om de bevolking van de gemeente en haar aangrenzende gemeenten die tevreden zijn met hun vrije tijd op te tellen, en een andere om de totale bevolking van de gemeente en haar aangrenzende gemeenten op te tellen. Het doel is om een gecombineerde tevredenheidsscore te berekenen door ook de aangrenzende gemeenten mee te nemen.
        - Het berekende totale aantal tevreden inwoners en het totale aantal inwoners werden vervolgens gebruikt om terug te rekenen naar het percentage tevreden inwoners.

    """,
    "Mediaan besteedbaar inkomen": """
        **Welkom bij Mediaan besteedbaar inkomen indicator**
        - Deze indicator is onderdeel van het Materiële welvaart
        - 2021 zijn voorlopige cijfers en de correctie voor de prijsverandering 
        - Meeteenheid: Euro per huishouden in constante prijzen in 2021
        - Voor deze indicator kan geen specifieke ruimtelijke spillover-/compensatieafstand worden aangenomen, omdat hierover geen relevante literatuur beschikbaar is. Daarom wordt in deze analyse een eerste-orde-contiguïteit (first order contiguity) toegepast. Dit betekent dat aangenomen wordt dat wanneer gemeenten een grens delen, het mediaan besteedbaar inkomen over deze grenzen heen overloopt. De gemiddelde waarde voor het mediaan besteedbaar inkomen per gemeente wordt gegeven door het CBS, als waarde per huishouden.
        - Om rekening te houden met de grootte van elke gemeente, moest de waarde van het mediaan besteedbaar inkomen worden vermenigvuldigd met het aantal huishoudens van de gemeente. Dit aantal is gebruikt in de verdere berekeningen.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over het mediaan besteedbaar inkomen geanalyseerd met behulp van ArcGIS Pro. Eerst werden aangrenzende gemeenten bepaald op basis van gedeelde grenzen, gedefinieerd als geometrieën die elkaar raken. Vervolgens werden voor elke gemeente twee variabelen geactiveerd: één om het totale aantal huishoudens van de gemeente en haar aangrenzende gemeenten op te tellen, en een andere om het totale besteedbare inkomen van alle huishoudens in de gemeente en haar aangrenzende gemeenten op te tellen. Het doel is om een gecombineerde score te berekenen door ook de aangrenzende gemeenten mee te nemen.
        - Het berekende totale besteedbaar inkomen en het totale aantal huishoudens werden vervolgens gebruikt om terug te rekenen naar het mediaan besteedbaar inkomen.
    """,
    "Overgewicht": """
        **Welkom bij Overgewicht indicator**
        - Deze indicator is onderdeel van het Gezondheid thema.
        - Voor de jaren 2012 en 2016 is de gemeten populatie 19+
        - Meeteenheid: percentage van de bevolking van 18 jaar en ouder is te zwaar
        - Voor deze indicator kan geen specifieke ruimtelijke spillover-/compensatieafstand worden aangenomen, omdat hierover geen relevante literatuur beschikbaar is. Daarom wordt in deze analyse een eerste-orde-contiguïteit (first order contiguity) toegepast. Dit betekent dat aangenomen wordt dat wanneer gemeenten een grens delen, overgewicht over deze grenzen heen overloopt. De gemiddelde waarde voor overgewicht per gemeente wordt gegeven door het CBS, als percentage van de bevolking van 18 jaar en ouder die overgewicht heeft.
        - Om rekening te houden met de bevolkingsgrootte van elke gemeente, moest het percentage van de inwoners van 18 jaar en ouder die overgewicht hebben, worden omgezet naar het totale aantal inwoners (18+) die overgewicht hebben. Aangezien de CBS-gegevens zijn verstrekt voor inwoners van 18 jaar en ouder, maar er geen gegevens zijn over het aantal inwoners in deze leeftijdsgroep, is de bevolking van 15 jaar en ouder gebruikt in de verdere berekeningen. De resultaten van de verdere berekeningen zullen waarschijnlijk verschillen van de resultaten als gegevens over de leeftijdsgroep van 18 jaar en ouder beschikbaar zouden zijn geweest.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over overgewicht geanalyseerd met behulp van ArcGIS Pro. Eerst werden aangrenzende gemeenten bepaald op basis van gedeelde grenzen, gedefinieerd als geometrieën die elkaar raken. Vervolgens werden voor elke gemeente twee variabelen geactiveerd: één om de bevolking van de gemeente en haar aangrenzende gemeenten die overgewicht hebben op te tellen, en een andere om de totale bevolking van de gemeente en haar aangrenzende gemeenten op te tellen. Het doel is om een gecombineerde score te berekenen door ook de aangrenzende gemeenten mee te nemen.
        - Het berekende totale aantal inwoners met overgewicht en het totale aantal inwoners werden vervolgens gebruikt om terug te rekenen naar het percentage inwoners met overgewicht.
    """,
    "Ervaren gezondheid": """
        **Welkom bij Ervaren gezondheid indicator**
        - Deze indicator is onderdeel van het Gezondheid thema.
        - Voor de jaren 2012 en 2016 is de gemeten populatie 19+
        - Meeteenheid: percentage van de bevolking van 18 jaar en ouder beschouwt zijn/haar eigen gezondheid als (zeer) goed
        - Voor deze indicator kan geen specifieke ruimtelijke spillover-/compensatieafstand worden aangenomen, omdat hierover geen relevante literatuur beschikbaar is. Daarom wordt in deze analyse een eerste-orde-contiguïteit (first order contiguity) toegepast. Dit betekent dat aangenomen wordt dat wanneer gemeenten een grens delen, ervaren gezondheid over deze grenzen heen overloopt. De gemiddelde waarde voor ervaren gezondheid per gemeente wordt gegeven door het CBS, als percentage van de bevolking van 18 jaar en ouder die hun gezondheid als (zeer) goed ervaren.
        - Om rekening te houden met de bevolkingsgrootte van elke gemeente, moest het percentage van de inwoners van 18 jaar en ouder die hun gezondheid als (zeer) goed ervaren, worden omgezet naar het totale aantal inwoners (18+) die hun gezondheid als (zeer) goed ervaren. Aangezien de CBS-gegevens zijn verstrekt voor inwoners van 18 jaar en ouder, maar er geen gegevens zijn over het aantal inwoners in deze leeftijdsgroep, is de bevolking van 15 jaar en ouder gebruikt in de verdere berekeningen. De resultaten van de verdere berekeningen zullen waarschijnlijk verschillen van de resultaten als gegevens over de leeftijdsgroep van 18 jaar en ouder beschikbaar zouden zijn geweest.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over ervaren gezondheid geanalyseerd met behulp van ArcGIS Pro. Eerst werden aangrenzende gemeenten bepaald op basis van gedeelde grenzen, gedefinieerd als geometrieën die elkaar raken. Vervolgens werden voor elke gemeente twee variabelen geactiveerd: één om de bevolking van de gemeente en haar aangrenzende gemeenten die hun gezondheid als (zeer) goed ervaren op te tellen, en een andere om de totale bevolking van de gemeente en haar aangrenzende gemeenten op te tellen. Het doel is om een gecombineerde score te berekenen door ook de aangrenzende gemeenten mee te nemen.
        - Het berekende totale aantal inwoners die hun gezondheid als (zeer) goed ervaren en het totale aantal inwoners werden vervolgens gebruikt om terug te rekenen naar het percentage inwoners die hun gezondheid als (zeer) goed ervaren.
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
        - Voor deze indicator kan geen specifieke ruimtelijke spillover-/compensatieafstand worden aangenomen, omdat hierover geen relevante literatuur beschikbaar is. Daarom wordt in deze analyse een eerste-orde-contiguïteit (first order contiguity) toegepast. Dit betekent dat aangenomen wordt dat wanneer gemeenten een grens delen, mensen met één of meer langdurige aandoeningen of ziektes over deze grenzen heen overlopen. De gemiddelde waarde voor mensen met één of meer langdurige aandoeningen of ziektes per gemeente wordt gegeven door het CBS, als percentage van de bevolking van 18 jaar en ouder die één of meer langdurige aandoeningen of ziektes heeft.
        - Om rekening te houden met de bevolkingsgrootte van elke gemeente, moest het percentage van de inwoners van 18 jaar en ouder die één of meer langdurige aandoeningen of ziektes hebben, worden omgezet naar het totale aantal inwoners (18+) die één of meer langdurige aandoeningen of ziektes hebben. Aangezien de CBS-gegevens zijn verstrekt voor inwoners van 18 jaar en ouder, maar er geen gegevens zijn over het aantal inwoners in deze leeftijdsgroep, is de bevolking van 15 jaar en ouder gebruikt in de verdere berekeningen. De resultaten van de verdere berekeningen zullen waarschijnlijk verschillen van de resultaten als gegevens over de leeftijdsgroep van 18 jaar en ouder beschikbaar zouden zijn geweest.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over mensen met één of meer langdurige aandoeningen of ziektes geanalyseerd met behulp van ArcGIS Pro. Eerst werden aangrenzende gemeenten bepaald op basis van gedeelde grenzen, gedefinieerd als geometrieën die elkaar raken. Vervolgens werden voor elke gemeente twee variabelen geactiveerd: één om de bevolking van de gemeente en haar aangrenzende gemeenten die één of meer langdurige aandoeningen of ziektes hebben op te tellen, en een andere om de totale bevolking van de gemeente en haar aangrenzende gemeenten op te tellen. Het doel is om een gecombineerde score te berekenen door ook de aangrenzende gemeenten mee te nemen.
        - Het berekende totale aantal inwoners die één of meer langdurige aandoeningen of ziektes hebben en het totale aantal inwoners werden vervolgens gebruikt om terug te rekenen naar het percentage inwoners die één of meer langdurige aandoeningen of ziektes hebben.
    """,
    "Nettoarbeidsparticipatie": """
        **Welkom bij Nettoarbeidsparticipatie indicator**
        - Deze indicator is onderdeel van het Arbeid en vrije tijd thema.
        - Meeteenheid: percentage van de bevolking van 15 tot 74 jaar
        - Voor deze indicator wordt gewerkt met een ruimtelijke spillover-/compensatieafstand van 25 km.
        - Dit betekent dat er wordt uitgegaan van het feit dat de netto arbeidsparticipatie gemiddeld gezien zich verspreidt tot 25 km van elke locatie, wat de invloed van nabijgelegen gebieden weergeeft. Het gemiddelde percentage van de bevolking dat bijdraagt aan de netto arbeidsparticipatie per gemeente wordt gegeven door het CBS, als een percentage van individuen van 15 tot 74 jaar die bijdragen aan de netto arbeidsparticipatie.
        - Om rekening te houden met de grootte van de bevolking van elke gemeente, is het percentage van de individuen van 15 tot 74 jaar die bijdragen aan de netto arbeidsparticipatie omgezet in het totale aantal individuen (behorend tot de werkende bevolking) die bijdraagt aan de netto arbeidsparticipatie. Omdat de CBS-gegevens echter zijn verstrekt voor individuen van 15 tot 74 jaar, maar de gegevens over het aantal individuen in deze leeftijdsgroep ontbreken, wordt de werkende bevolking (15 tot 64 jaar) gebruikt in de verdere berekeningen. De resultaten van de berekeningen zullen waarschijnlijk verschillen van wanneer gegevens voor de leeftijdsgroep 15 tot 74 jaar beschikbaar zouden zijn.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over netto arbeidsparticipatie geanalyseerd met behulp van ArcGIS Pro. Eerst zijn de gemeentelijke polygonen (met gegevens over netto arbeidsparticipatie) omgezet in rastercellen van 100x100 meter. Dit werd gedaan door twee aparte rasterlagen te maken: een die het aantal inwoners representeert die bijdragen aan de netto arbeidsparticipatie, en de andere die de totale werkende bevolking representeert. Voor beide rasterlagen kreeg elke rastercel de waarde van het bijbehorende gemeentelijke polygoon.
        - Vervolgens werden focale statistieken toegepast op beide rasterlagen afzonderlijk. Dit gebeurde door de gemiddelde waarde voor elke rastercel te berekenen op basis van de omliggende cellen. Door een cirkelvormige neighborhood met een straal van 25 km te gebruiken, wordt een gemiddelde berekend van alle waarden van rastercellen binnen deze straal, zodat het spillover effect van netto arbeidsparticipatie en de invloed van nabijgelegen gemeenten wordt meegenomen.
        - Door gebruik te maken van zone-statistieken worden de geüpdatete rastercellen samengevat naar de gemeentelijke polygonen voor beide rasterlagen. Voor elk gemeentelijk polygoon werd de gemiddelde waarde berekend van alle rastercellen die binnen de grenzen van het polygoon vallen. Dit werd gedaan voor zowel het aantal individuen die bijdragen aan de netto arbeidsparticipatie, als voor de totale werkende bevolking. Deze twee waarden werden vervolgens gebruikt om het percentage van de individuen die bijdragen aan de netto arbeidsparticipatie binnen de werkende bevolking opnieuw te berekenen, aangepast voor het ruimtelijke spillover-effect over gemeentegrenzen.
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
        - Voor deze indicator wordt gewerkt met een ruimtelijke spillover-/compensatieafstand van 25 km.
        - Dit betekent dat er wordt uitgegaan van het feit dat werkloosheid gemiddeld gezien zich verspreidt tot 25 km van elke locatie, wat de invloed van nabijgelegen gebieden weergeeft. De gemiddelde werkloosheid per gemeente wordt gegeven door het CBS, als een percentage van de werkende bevolking die werkloos is.
        - Om rekening te houden met de grootte van de bevolking van elke gemeente, is het percentage van de werkende bevolking die werkloos is omgezet in het totale aantal werklozen (behorend tot de werkende bevolking). Dit aantal is gebruikt in de verdere berekeningen.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over werkloosheid geanalyseerd met behulp van ArcGIS Pro. Eerst zijn de gemeentelijke polygonen (met gegevens over werkloosheid) omgezet in rastercellen van 100x100 meter. Dit werd gedaan door twee aparte rasterlagen te maken: een die het aantal werklozen representeert, en de andere die de totale werkende bevolking representeert. Voor beide rasterlagen kreeg elke rastercel de waarde van het bijbehorende gemeentelijke polygoon.
        - Vervolgens werden focale statistieken toegepast op beide rasterlagen afzonderlijk. Dit gebeurde door de gemiddelde waarde voor elke rastercel te berekenen op basis van de omliggende cellen. Door een cirkelvormige neighborhood met een straal van 25 km te gebruiken, wordt een gemiddelde berekend van alle waarden van rastercellen binnen deze straal, zodat het spillover effect van werkloosheid en de invloed van nabijgelegen gemeenten wordt meegenomen.
        - Door gebruik te maken van zone-statistieken worden de geüpdatete rastercellen samengevat naar de gemeentelijke polygonen voor beide rasterlagen. Voor elk gemeentelijk polygoon werd de gemiddelde waarde berekend van alle rastercellen die binnen de grenzen van het polygoon vallen. Dit werd gedaan voor zowel het aantal werklozen, als voor de totale werkende bevolking. Deze twee waarden werden vervolgens gebruikt om het percentage werklozen binnen de werkende bevolking opnieuw te berekenen, aangepast voor het ruimtelijke spillover-effect over gemeentegrenzen.
    """,
    "Bevolking met een startkwalificatie": """
        **Welkom bij Bevolking met een startkwalificatie indicator**
        - Deze indicator is onderdeel van het Arbeid en vrije tijd thema.
        - Voor deze indicator wordt gewerkt met een ruimtelijke spillover-/compensatieafstand van 25 km.
        - Dit betekent dat er wordt uitgegaan van het feit dat de bevolking met een startkwalificatie gemiddeld gezien zich verspreidt tot 25 km van elke locatie, wat de invloed van nabijgelegen gebieden weergeeft. Het gemiddelde percentage van de bevolking met een startkwalificatie per gemeente wordt gegeven door het CBS, als een percentage van de individuen van 15 tot 74 jaar die een startkwalificatie hebben.
        - Om rekening te houden met de grootte van de bevolking van elke gemeente, is het percentage van de individuen van 15 tot 74 jaar die een startkwalificatie hebben omgezet in het totale aantal individuen (behorend tot de werkende bevolking) die een startkwalificatie hebben. Omdat de CBS-gegevens echter zijn verstrekt voor individuen van 15 tot 74 jaar, maar de gegevens over het aantal individuen in deze leeftijdsgroep ontbreken, wordt de werkende bevolking (15 tot 64 jaar) gebruikt in de verdere berekeningen. De resultaten van de berekeningen zullen waarschijnlijk verschillen van wanneer gegevens voor de leeftijdsgroep 15 tot 74 jaar beschikbaar zouden zijn.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over de bevolking met een startkwalificatie geanalyseerd met behulp van ArcGIS Pro. Eerst zijn de gemeentelijke polygonen (met gegevens over de bevolking met een startkwalificatie) omgezet in rastercellen van 100x100 meter. Dit werd gedaan door twee aparte rasterlagen te maken: een die het aantal individuen met een startkwalificatie representeert, en de andere die de totale werkende bevolking representeert. Voor beide rasterlagen kreeg elke rastercel de waarde van het bijbehorende gemeentelijke polygoon.
        - Vervolgens werden focale statistieken toegepast op beide rasterlagen afzonderlijk. Dit gebeurde door de gemiddelde waarde voor elke rastercel te berekenen op basis van de omliggende cellen. Door een cirkelvormige neighborhood met een straal van 25 km te gebruiken, wordt een gemiddelde berekend van alle waarden van rastercellen binnen deze straal, zodat het spillover effect van bevolking met een startkwalificatie en de invloed van nabijgelegen gemeenten wordt meegenomen.
        - Door gebruik te maken van zone-statistieken worden de geüpdatete rastercellen samengevat naar de gemeentelijke polygonen voor beide rasterlagen. Voor elk gemeentelijk polygoon werd de gemiddelde waarde berekend van alle rastercellen die binnen de grenzen van het polygoon vallen. Dit werd gedaan voor zowel het aantal individuen met een startkwalificatie, als voor de totale werkende bevolking. Deze twee waarden werden vervolgens gebruikt om het percentage van de bevolking met een startkwalificatie binnen de werkende bevolking opnieuw te berekenen, aangepast voor het ruimtelijke spillover-effect over gemeentegrenzen.
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
        - Voor deze indicator wordt gewerkt met een ruimtelijke spillover-/compensatieafstand van 791 meter. Dit betekent dat er aangenomen wordt dat men gemiddeld bereid is om 791 meter te reizen voor het openbaar vervoer. De gemiddelde afstanden tot het openbaar vervoer per gemeente zijn gegeven door het CBS, maar deze dataset bevat geen informatie over het type openbaar vervoer waar het om gaat.
        - Onderzoek toont aan dat mensen bereid zijn de kortste afstand af te leggen naar een bushalte en (iets) langere afstanden naar andere soorten openbaar vervoer. Vanwege het gebrek aan gegevens over het vervoerstype gaat de berekening uit van het type met de kortste reisafstand: bushaltes. Als er informatie beschikbaar was over het type openbaar vervoer, zouden de resultaten van de berekening waarschijnlijk anders zijn.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over de gemiddelde afstanden tot het openbaar vervoer geanalyseerd met behulp van ArcGIS Pro. Eerst zijn de gemeentelijke polygonen (met gegevens over de afstand tot het openbaar vervoer) omgezet in rastercellen van 100x100 meter. Elke rastercel kreeg de waarde van het bijbehorende gemeentelijke polygoon. Vervolgens zijn focale statistieken toegepast om de gemiddelde waarde voor elke rastercel te berekenen op basis van de omliggende cellen. Door een cirkelvormige neighborhood met een straal van 791 meter te gebruiken, wordt een gemiddelde berekend van alle waarden van rastercellen binnen deze straal, zodat het spillover effect van afstanden tot sportvelden en de invloed van nabijgelegen gemeenten wordt meegenomen.
        - Met behulp van zone-statistieken zijn de geüpdatete rastercellen terug gerekend naar de gemeentelijke polygonen. Voor elk gemeentelijk polygoon is de gemiddelde waarde van alle rastercellen binnen de grenzen berekend. Dit resulteert in één waarde voor de afstand tot het openbaar vervoer per gemeente, waarbij rekening wordt gehouden met reizen over gemeentegrenzen.
        - Ten slotte, als de berekende ruimtelijke spillover afstand groter is dan de oorspronkelijke waarde, blijft de oorspronkelijke waarde behouden. Dit betekent dat de oorspronkelijke waarde alleen wordt bijgewerkt wanneer er een compenserende ruimtelijke spillover tussen gemeenten is, ervan uitgaande dat individuen niet verder reizen naar een aangrenzende gemeente als de voorziening dichterbij beschikbaar is in hun eigen woonplaats.
    """,
    "Afstand tot sportterrein": """
        **Welkom bij Afstand tot sportterrein indicator**
        - Deze indicator is onderdeel van het Wonen thema.
        - Meeteenheid: kilometers
        - Voor deze indicator wordt gewerkt met een een ruimtelijke spillover-/compensatieafstand van 1 km. Dit betekent dat er aangenomen wordt dat men gemiddeld bereid is om 1 km te reizen voor toegang tot sport. De gemiddelde afstanden tot sportvelden per gemeente zijn verstrekt door het CBS.
        - Om gemeentelijke spillovers in rekening te brengen, zijn de CBS-gegevens over de gemiddelde afstanden tot sport geanalyseerd met behulp van ArcGIS Pro. Eerst zijn de gemeentelijke polygonen (met gegevens over de afstand tot sportvelden) omgezet in rastercellen van 100x100 meter. Elke rastercel kreeg de waarde van het bijbehorende gemeentelijke polygoon. Vervolgens zijn focale statistieken toegepast om de gemiddelde waarde voor elke rastercel te berekenen op basis van de omliggende cellen. Door een cirkelvormige neighborhood met een straal van 1000 meter te gebruiken, wordt een gemiddelde berekend van alle waarden van rastercellen binnen deze straal, zodat het spillover effect van afstanden tot sportvelden en de invloed van nabijgelegen gemeenten wordt meegenomen.
        - Met behulp van zone-statistieken zijn de geüpdatete rastercellen terug gerekend naar de gemeentelijke polygonen. Voor elk gemeentelijk polygoon is de gemiddelde waarde van alle rastercellen binnen de grenzen berekend. Dit resulteert in één waarde voor de afstand tot sportvelden per gemeente, waarbij rekening wordt gehouden met reizen over gemeentegrenzen.
        - Ten slotte, als de berekende ruimtelijke spillover afstand groter is dan de oorspronkelijke waarde, blijft de oorspronkelijke waarde behouden. Dit betekent dat de oorspronkelijke waarde alleen wordt bijgewerkt wanneer er een compenserende ruimtelijke spillover tussen gemeenten is, ervan uitgaande dat individuen niet verder reizen naar een aangrenzende gemeente als de voorziening dichterbij beschikbaar is in hun eigen woonplaats.

    """,
    "Tevredenheid met woonomgeving": """
        **Welkom bij Tevredenheid met woonomgeving indicator**
        - Deze indicator is onderdeel van het Wonen thema.
        - Meeteenheid: percentage particuliere huishoudens dat (zeer) tevreden is
        - Voor deze indicator kan geen specifieke ruimtelijke spillover-/compensatieafstand worden aangenomen, omdat hierover geen relevante literatuur beschikbaar is. Daarom wordt in deze analyse een eerste-orde-contiguïteit (first order contiguity) toegepast. Dit betekent dat aangenomen wordt dat wanneer gemeenten een grens delen, tevredenheid met de woonomgeving over deze grenzen heen overloopt. De gemiddelde waarde voor tevredenheid met de woonomgeving per gemeente wordt gegeven door het CBS, als percentage van de huishoudens die tevreden zijn met hun woonomgeving.
        - Om rekening te houden met de bevolkingsgrootte van elke gemeente, moest het percentage van de huishoudens die tevreden zijn met hun woonomgeving, worden omgezet naar het totale aantal huishoudens die tevreden zijn met hun woonomgeving. Dit aantal is gebruikt in de verdere berekeningen.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over tevredenheid met de woonomgeving geanalyseerd met behulp van ArcGIS Pro. Eerst werden aangrenzende gemeenten bepaald op basis van gedeelde grenzen, gedefinieerd als geometrieën die elkaar raken. Vervolgens werden voor elke gemeente twee variabelen geactiveerd: één om de huishoudens van de gemeente en haar aangrenzende gemeenten die tevreden zijn met hun woonomgeving op te tellen, en een andere om het totale aantal huishoudens van de gemeente en haar aangrenzende gemeenten op te tellen. Het doel is om een gecombineerde score te berekenen door ook de aangrenzende gemeenten mee te nemen.
        - Het berekende totale aantal huishoudens die tevreden zijn met hun woonomgeving en het totale aantal huishoudens werden vervolgens gebruikt om terug te rekenen naar het percentage huishoudens die tevreden zijn met hun woonomgeving.
    """,
    "Tevredenheid met woning": """
        **Welkom bij Tevredenheid met woning indicator**
        - Deze indicator is onderdeel van het Wonen thema.
        - Meeteenheid: percentage particuliere huishoudens dat (zeer) tevreden is
        - Voor deze indicator kan geen specifieke ruimtelijke spillover-/compensatieafstand worden aangenomen, omdat hierover geen relevante literatuur beschikbaar is. Daarom wordt in deze analyse een eerste-orde-contiguïteit (first order contiguity) toegepast. Dit betekent dat aangenomen wordt dat wanneer gemeenten een grens delen, tevredenheid met de woning over deze grenzen heen overloopt. De gemiddelde waarde voor tevredenheid met de woning per gemeente wordt gegeven door het CBS, als percentage van de huishoudens die tevreden zijn met hun woning.
        - Om rekening te houden met de bevolkingsgrootte van elke gemeente, moest het percentage van de huishoudens die tevreden zijn met hun woning, worden omgezet naar het totale aantal huishoudens die tevreden zijn met hun woning. Dit aantal is gebruikt in de verdere berekeningen.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over tevredenheid met de woning geanalyseerd met behulp van ArcGIS Pro. Eerst werden aangrenzende gemeenten bepaald op basis van gedeelde grenzen, gedefinieerd als geometrieën die elkaar raken. Vervolgens werden voor elke gemeente twee variabelen geactiveerd: één om de huishoudens van de gemeente en haar aangrenzende gemeenten die tevreden zijn met hun woning op te tellen, en een andere om het totale aantal huishoudens van de gemeente en haar aangrenzende gemeenten op te tellen. Het doel is om een gecombineerde score te berekenen door ook de aangrenzende gemeenten mee te nemen.
        - Het berekende totale aantal huishoudens die tevreden zijn met hun woning en het totale aantal huishoudens werden vervolgens gebruikt om terug te rekenen naar het percentage huishoudens die tevreden zijn met hun woning.
    """,
    "Geregistreerde problematische schulden": """
        **Welkom bij Geregistreerde problematische schulden indicator**
        - Deze indicator is onderdeel van het Materiële welvaart thema.
        - Voor deze indicator kan geen specifieke ruimtelijke spillover-/compensatieafstand worden aangenomen, omdat hierover geen relevante literatuur beschikbaar is. Daarom wordt in deze analyse een eerste-orde-contiguïteit (first order contiguity) toegepast. Dit betekent dat aangenomen wordt dat wanneer gemeenten een grens delen, geregistreerde problematische schulden over deze grenzen heen overlopen. De gemiddelde waarde voor geregistreerde problematische schulden per gemeente wordt gegeven door het CBS, als percentage van de huishoudens die geregistreerde problematische schulden hebben.
        - Om rekening te houden met de bevolkingsgrootte van elke gemeente, moest het percentage van de huishoudens die geregistreerde problematische schulden hebben, worden omgezet naar het totale aantal huishoudens die geregistreerde problematische schulden hebben. Dit aantal is gebruikt in de verdere berekeningen.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over geregistreerde problematische schulden geanalyseerd met behulp van ArcGIS Pro. Eerst werden aangrenzende gemeenten bepaald op basis van gedeelde grenzen, gedefinieerd als geometrieën die elkaar raken. Vervolgens werden voor elke gemeente twee variabelen geactiveerd: één om de huishoudens van de gemeente en haar aangrenzende gemeenten die geregistreerde problematische schulden hebben op te tellen, en een andere om het totale aantal huishoudens van de gemeente en haar aangrenzende gemeenten op te tellen. Het doel is om een gecombineerde score te berekenen door ook de aangrenzende gemeenten mee te nemen.
        - Het berekende totale aantal huishoudens die geregistreerde problematische schulden hebben en het totale aantal huishoudens werden vervolgens gebruikt om terug te rekenen naar het percentage huishoudens die geregistreerde problematische schulden hebben.
    """,
    "Afstand tot basisschool": """
        **Welkom bij Afstand tot basisschool indicator**
        - Deze indicator is onderdeel van het Wonen thema.
        - Meeteenheid: kilometers
        - Voor deze indicator wordt gewerkt met een een ruimtelijke spillover-/compensatieafstand van 4023 meter. Dit betekent dat er aangenomen wordt dat men gemiddeld bereid is om 4023 meter te reizen voor toegang tot een basisschool. De gemiddelde afstanden tot basisscholen per gemeente zijn verstrekt door het CBS.
        - Om gemeentelijke spillovers in rekening te brengen, zijn de CBS-gegevens over de gemiddelde afstanden tot een basisschool geanalyseerd met behulp van ArcGIS Pro. Eerst zijn de gemeentelijke polygonen (met gegevens over de afstand tot een basisschool) omgezet in rastercellen van 100x100 meter. Elke rastercel kreeg de waarde van het bijbehorende gemeentelijke polygoon. Vervolgens zijn focale statistieken toegepast om de gemiddelde waarde voor elke rastercel te berekenen op basis van de omliggende cellen. Door een cirkelvormige neighborhood met een straal van 4023 meter te gebruiken, wordt een gemiddelde berekend van alle waarden van rastercellen binnen deze straal, zodat het spillover effect van afstanden tot basisscholen en de invloed van nabijgelegen gemeenten wordt meegenomen.
        - Met behulp van zone-statistieken zijn de geüpdatete rastercellen terug gerekend naar de gemeentelijke polygonen. Voor elk gemeentelijk polygoon is de gemiddelde waarde van alle rastercellen binnen de grenzen berekend. Dit resulteert in één waarde voor de afstand tot een basisschool per gemeente, waarbij rekening wordt gehouden met reizen over gemeentegrenzen.
        - Ten slotte, als de berekende ruimtelijke spillover afstand groter is dan de oorspronkelijke waarde, blijft de oorspronkelijke waarde behouden. Dit betekent dat de oorspronkelijke waarde alleen wordt bijgewerkt wanneer er een compenserende ruimtelijke spillover tussen gemeenten is, ervan uitgaande dat individuen niet verder reizen naar een aangrenzende gemeente als de voorziening dichterbij beschikbaar is in hun eigen woonplaats.

    """,
    "Afstand tot café e.d.": """
        **Welkom bij Afstand tot café e.d. indicator**
        - Deze indicator is onderdeel van het Wonen thema.
        - Meeteenheid: kilometers
        - Voor deze indicator wordt er gewerkt met een ruimtelijke spillover-/compensatieafstand van 4184 meter. Dit betekent dat er wordt uitgegaan van het feit dat men gemiddeld bereid is om 4184 meter te reizen voor toegang tot café’s enz. De gemiddelde afstanden tot café’s enz. per gemeente zijn gegeven door het CBS.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over de gemiddelde afstanden tot café’s enz. geanalyseerd met behulp van ArcGIS Pro. Eerst zijn de gemeentelijke polygonen (met gegevens over de afstand tot café’s enz.) omgezet in rastercellen van 100x100 meter. Elke rastercel kreeg de waarde van het bijbehorende gemeentelijke polygoon. Vervolgens zijn focale statistieken toegepast om de gemiddelde waarde voor elke rastercel te berekenen op basis van de omliggende cellen. Door een cirkelvormige neighborhood met een straal van 4184 meter te gebruiken, wordt een gemiddelde berekend van alle waarden van rastercellen binnen deze straal, zodat het spillover effect van afstanden tot café’s etc. en de invloed van nabijgelegen gemeenten wordt meegenomen.
        - Met behulp van zone-statistieken zijn de geüpdatete rastercellen terug gerekend naar de gemeentelijke polygonen. Voor elk gemeentelijk polygoon is de gemiddelde waarde van alle rastercellen binnen de grenzen berekend. Dit resulteert in één waarde voor de afstand tot café’s enz. per gemeente, waarbij rekening wordt gehouden met reizen over gemeentegrenzen heen.
        - Ten slotte, als de berekende ruimtelijke spillover afstand groter is dan de oorspronkelijke waarde, blijft de oorspronkelijke waarde behouden. Dit betekent dat de oorspronkelijke waarde alleen wordt bijgewerkt wanneer er een compenserende ruimtelijke spillover tussen gemeenten is, ervan uitgaande dat individuen niet verder reizen naar een aangrenzende gemeente als de voorziening dichterbij beschikbaar is in hun eigen woonplaats.

    """,
    "Contact met familie, vrienden of buren": """
        **Welkom bij Contact met familie, vrienden of buren indicator**
        - Deze indicator is onderdeel van het Samenleving thema.
        - Voorlopige cijfers. Bij het toevoegen van een nieuw jaar schat het model alle jaren uit de reeks opnieuw. Raadpleeg de Technische Toelichting voor meer uitleg over de interpretatie van de modelschattingen en de marges.
        - Meeteenheid: percentage van de bevolking van 15+ dat gemiddeld minstens één keer per week met iemand in contact komt
        - Voor deze indicator kan geen specifieke ruimtelijke spillover-/compensatieafstand worden aangenomen, omdat hierover geen relevante literatuur beschikbaar is. Daarom wordt in deze analyse een eerste-orde-contiguïteit (first order contiguity) toegepast. Dit betekent dat aangenomen wordt dat wanneer gemeenten een grens delen, contact met familie, vrienden of buren over deze grenzen heen overloopt. De gemiddelde waarde voor contact met familie, vrienden of buren per gemeente wordt gegeven door het CBS, als percentage van de bevolking van 15 jaar en ouder die ten minste één keer per week contact heeft met familie, vrienden of buren.
        - Om rekening te houden met de bevolkingsgrootte van elke gemeente, moest het percentage van de inwoners van 15 jaar en ouder die ten minste één keer per week contact hebben met familie, vrienden of buren, worden omgezet naar het totale aantal inwoners (15+) die ten minste één keer per week contact hebben met familie, vrienden of buren. Dit aantal is gebruikt in de verdere berekeningen.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over contact met familie, vrienden of buren geanalyseerd met behulp van ArcGIS Pro. Eerst werden aangrenzende gemeenten bepaald op basis van gedeelde grenzen, gedefinieerd als geometrieën die elkaar raken. Vervolgens werden voor elke gemeente twee variabelen geactiveerd: één om de bevolking van de gemeente en haar aangrenzende gemeenten die ten minste één keer per week contact hebben met familie, vrienden of buren op te tellen, en een andere om de totale bevolking van de gemeente en haar aangrenzende gemeenten op te tellen. Het doel is om een gecombineerde score te berekenen door ook de aangrenzende gemeenten mee te nemen.
        - Het berekende totale aantal inwoners die ten minste één keer per week contact hebben met familie, vrienden of buren en het totale aantal inwoners werden vervolgens gebruikt om terug te rekenen naar het percentage inwoners die ten minste één keer per week contact hebben met familie, vrienden of buren.
    """,
    "Vertrouwen in instituties": """
        **Welkom bij Vertrouwen in instituties indicator**
        - Deze indicator is onderdeel van het Samenleving thema.
        - Voorlopige cijfers. Bij het toevoegen van een nieuw jaar schat het model alle jaren uit de reeks opnieuw. Raadpleeg de Technische Toelichting voor meer uitleg over de interpretatie van de modelschattingen en de marges.
        - Meeteenheid: percentage van de bevolking van 15+ heeft voldoende vertrouwen
        - Voor deze indicator wordt gewerkt met een ruimtelijke spillover-/compensatieafstand van 41,05 km. Dit betekent dat er wordt uitgegaan van het feit dat vertrouwen in instituties gemiddeld gezien zich verspreidt tot 41,05 km van elke locatie, wat de invloed van nabijgelegen gebieden weergeeft. Het gemiddelde vertrouwen in instituties per gemeente is gegeven door het CBS, als een percentage van de bevolking van 15 jaar en ouder die voldoende vertrouwen heeft in instituties.
        - Om rekening te houden met de grootte van de bevolking van elke gemeente, is het percentage van de bevolking van 15 jaar en ouder die voldoende vertrouwen heeft in instituties omgezet in het totale aantal individuen (van 15 jaar en ouder) die voldoende vertrouwen hebben. Dit aantal is gebruikt in de verdere berekeningen.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over vertrouwen in instituties geanalyseerd met behulp van ArcGIS Pro. Eerst zijn de gemeentelijke polygonen (met gegevens over vertrouwen in instituties) omgezet in rastercellen van 100x100 meter. Dit werd gedaan door twee aparte rasterlagen te maken: een die het aantal inwoners van 15 jaar en ouder met voldoende vertrouwen in instituties representeert, en de andere die de totale bevolking van 15 jaar en ouder representeert. Voor beide rasterlagen kreeg elke rastercel de waarde van het bijbehorende gemeentelijke polygoon.
        - Vervolgens werden focale statistieken toegepast op beide rasterlagen afzonderlijk. Dit gebeurde door de gemiddelde waarde voor elke rastercel te berekenen op basis van de omliggende cellen. Door een cirkelvormige neighborhood met een straal van 41050 meter te gebruiken, wordt een gemiddelde berekend van alle waarden van rastercellen binnen deze straal, zodat het spillover effect van vertrouwen in instituties en de invloed van nabijgelegen gemeenten wordt meegenomen.
        - Door gebruik te maken van zone-statistieken worden de geüpdatete rastercellen samengevat naar de gemeentelijke polygonen voor beide rasterlagen. Voor elk gemeentelijk polygoon werd de gemiddelde waarde berekend van alle rastercellen die binnen de grenzen van het polygoon vallen. Dit werd gedaan voor zowel het aantal inwoners van 15 jaar en ouder met voldoende vertrouwen in instituties, als voor de totale bevolking van 15 jaar en ouder. Deze twee waarden werden vervolgens gebruikt om het percentage van de bevolking van 15 jaar en ouder met voldoende vertrouwen in instituties opnieuw te berekenen, aangepast voor het ruimtelijke spillover-effect over gemeentegrenzen.
    """,
    "Vertrouwen in anderen": """
        **Welkom bij Vertrouwen in anderen indicator**
        -Deze indicator is onderdeel van het Samenleving thema.
        -Voorlopige cijfers. Bij het toevoegen van een nieuw jaar schat het model alle jaren uit de reeks opnieuw. Raadpleeg de Technische Toelichging voor meer uitleg over de interpretatie van de modelschattingen en de marges.
        - Meeteenheid: percentage van de bevolking van 15+ vindt de meeste mensen betrouwbaar
        - Voor deze indicator wordt gewerkt met een ruimtelijke spillover-/compensatieafstand van 41,05 km. Dit betekent dat er wordt uitgegaan van het feit dat vertrouwen in anderen gemiddeld gezien zich verspreidt tot 41,05 km van elke locatie, wat de invloed van nabijgelegen gebieden weergeeft. Het gemiddelde vertrouwen in anderen per gemeente wordt gegeven door het CBS, als een percentage van de bevolking van 15 jaar en ouder die voldoende vertrouwen heeft in anderen.
        - Om rekening te houden met de grootte van de bevolking van elke gemeente, is het percentage van de bevolking van 15 jaar en ouder die voldoende vertrouwen heeft in anderen omgezet in het totale aantal individuen (van 15 jaar en ouder) die voldoende vertrouwen hebben. Dit aantal is gebruikt in de verdere berekeningen.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over vertrouwen in anderen geanalyseerd met behulp van ArcGIS Pro. Eerst zijn de gemeentelijke polygonen (met gegevens over vertrouwen in anderen) omgezet in rastercellen van 100x100 meter. Dit werd gedaan door twee aparte rasterlagen te maken: een die het aantal inwoners van 15 jaar en ouder met voldoende vertrouwen in anderen representeert, en de andere die de totale bevolking van 15 jaar en ouder representeert. Voor beide rasterlagen kreeg elke rastercel de waarde van het bijbehorende gemeentelijke polygoon.
        - Vervolgens werden focale statistieken toegepast op beide rasterlagen afzonderlijk. Dit gebeurde door de gemiddelde waarde voor elke rastercel te berekenen op basis van de omliggende cellen. Door een cirkelvormige neighborhood met een straal van 41050 meter te gebruiken, wordt een gemiddelde berekend van alle waarden van rastercellen binnen deze straal, zodat het spillover effect van vertrouwen in anderen en de invloed van nabijgelegen gemeenten wordt meegenomen.
        - Door gebruik te maken van zone-statistieken worden de geüpdatete rastercellen samengevat naar de gemeentelijke polygonen voor beide rasterlagen. Voor elk gemeentelijk polygoon werd de gemiddelde waarde berekend van alle rastercellen die binnen de grenzen van het polygoon vallen. Dit werd gedaan voor zowel het aantal inwoners van 15 jaar en ouder met voldoende vertrouwen in anderen, als voor de totale bevolking van 15 jaar en ouder. Deze twee waarden werden vervolgens gebruikt om het percentage van de bevolking van 15 jaar en ouder met voldoende vertrouwen in anderen opnieuw te berekenen, aangepast voor het ruimtelijke spillover-effect over gemeentegrenzen.
     """,
    "Vrijwilligerswerk": """
        **Welkom bij Vrijwilligerswerk indicator**
        - Deze indicator is onderdeel van het Samenleving thema.
        - Voorlopige cijfers. Bij het toevoegen van een nieuw jaar schat het model alle jaren uit de reeks opnieuw. Raadpleeg de Technische Toelichging voor meer uitleg over de interpretatie van de modelschattingen en de marges.
        - Meeteenheid: percentage van de bevolking van 15 jaar en ouder dat georganiseerd vrijwilligerswerk doet
        - Voor deze indicator kan geen specifieke ruimtelijke spillover-/compensatieafstand worden aangenomen, omdat hierover geen relevante literatuur beschikbaar is. Daarom wordt in deze analyse een eerste-orde-contiguïteit (first order contiguity) toegepast. Dit betekent dat aangenomen wordt dat wanneer gemeenten een grens delen, vrijwilligerswerk over deze grenzen heen overloopt. De gemiddelde waarde voor vrijwilligerswerk per gemeente wordt gegeven door het CBS, als percentage van de bevolking van 15 jaar en ouder die vrijwilligerswerk doet.
        - Om rekening te houden met de bevolkingsgrootte van elke gemeente, moest het percentage van de inwoners van 15 jaar en ouder die vrijwilligerswerk doen, worden omgezet naar het totale aantal inwoners (15+) die vrijwilligerswerk doen. Dit aantal is gebruikt in de verdere berekeningen.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over vrijwilligerswerk geanalyseerd met behulp van ArcGIS Pro. Eerst werden aangrenzende gemeenten bepaald op basis van gedeelde grenzen, gedefinieerd als geometrieën die elkaar raken. Vervolgens werden voor elke gemeente twee variabelen geactiveerd: één om de bevolking van de gemeente en haar aangrenzende gemeenten die vrijwilligerswerk doen op te tellen, en een andere om de totale bevolking van de gemeente en haar aangrenzende gemeenten op te tellen. Het doel is om een gecombineerde score te berekenen door ook de aangrenzende gemeenten mee te nemen.
        - Het berekende totale aantal inwoners die vrijwilligerswerk doen en het totale aantal inwoners werden vervolgens gebruikt om terug te rekenen naar het percentage inwoners die vrijwilligerswerk doen.
    """,
    "Vaak onveilig gevoel in de buurt": """
        **Welkom bij Vaak onveilig voelen in de buurt indicator**
        - Deze indicator is onderdeel van het Veiligheid thema.
        - Meeteenheid: percentage van de bevolking van 15 jaar en ouder
        - Voor deze indicator kan geen specifieke ruimtelijke spillover-/compensatieafstand worden aangenomen, omdat hierover geen relevante literatuur beschikbaar is. Daarom wordt in deze analyse een eerste-orde-contiguïteit (first order contiguity) toegepast. Dit betekent dat aangenomen wordt dat wanneer gemeenten een grens delen, een vaak onveilig gevoel in de buurt over deze grenzen heen overloopt. De gemiddelde waarde voor een vaak onveilig gevoel in de buurt per gemeente wordt gegeven door het CBS, als percentage van de bevolking van 15 jaar en ouder die zich vaak onveilig voelt in de buurt.
        - Om rekening te houden met de bevolkingsgrootte van elke gemeente, moest het percentage van de inwoners van 15 jaar en ouder die zich vaak onveilig voelen in de buurt, worden omgezet naar het totale aantal inwoners (15+) die zich vaak onveilig voelen in de buurt. Dit aantal is gebruikt in de verdere berekeningen.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over een vaak onveilig gevoel in de buurt geanalyseerd met behulp van ArcGIS Pro. Eerst werden aangrenzende gemeenten bepaald op basis van gedeelde grenzen, gedefinieerd als geometrieën die elkaar raken. Vervolgens werden voor elke gemeente twee variabelen geactiveerd: één om de bevolking van de gemeente en haar aangrenzende gemeenten die zich vaak onveilig voelen in de buurt op te tellen, en een andere om de totale bevolking van de gemeente en haar aangrenzende gemeenten op te tellen. Het doel is om een gecombineerde score te berekenen door ook de aangrenzende gemeenten mee te nemen.
        - Het berekende totale aantal inwoners die zich vaak onveilig voelen in de buurt en het totale aantal inwoners werden vervolgens gebruikt om terug te rekenen naar het percentage inwoners die zich vaak onveilig voelen in de buurt.
    """,
    "Tevredenheid met sociaal leven": """
        **Welkom bij Tevredenheid met sociaal leven indicator**
        - Deze indicator is onderdeel van het Samenleving thema.
        - Voor deze indicator kan geen specifieke ruimtelijke spillover-/compensatieafstand worden aangenomen, omdat hierover geen relevante literatuur beschikbaar is. Daarom wordt in deze analyse een eerste-orde-contiguïteit (first order contiguity) toegepast. Dit betekent dat aangenomen wordt dat wanneer gemeenten een grens delen, tevredenheid met het sociale leven over deze grenzen heen overloopt. De gemiddelde waarde voor tevredenheid met het sociale leven per gemeente wordt gegeven door het CBS, als percentage van de bevolking van 18 jaar en ouder die tevreden is met hun sociale leven.
        - Om rekening te houden met de bevolkingsgrootte van elke gemeente, moest het percentage van de inwoners van 18 jaar en ouder die tevreden zijn met hun sociale leven, worden omgezet naar het totale aantal inwoners (18+) die tevreden zijn. Aangezien de CBS-gegevens zijn verstrekt voor inwoners van 18 jaar en ouder, maar er geen gegevens zijn over het aantal inwoners in deze leeftijdsgroep, is de bevolking van 15 jaar en ouder gebruikt in de verdere berekeningen. De resultaten van de verdere berekeningen zullen waarschijnlijk verschillen van de resultaten als gegevens over de leeftijdsgroep van 18 jaar en ouder beschikbaar zouden zijn geweest.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over tevredenheid met het sociale leven geanalyseerd met behulp van ArcGIS Pro. Eerst werden aangrenzende gemeenten bepaald op basis van gedeelde grenzen, gedefinieerd als geometrieën die elkaar raken. Vervolgens werden voor elke gemeente twee variabelen geactiveerd: één om de bevolking van de gemeente en haar aangrenzende gemeenten die tevreden zijn met hun sociale leven op te tellen, en een andere om de totale bevolking van de gemeente en haar aangrenzende gemeenten op te tellen. Het doel is om een gecombineerde score te berekenen door ook de aangrenzende gemeenten mee te nemen.
        - Het berekende totale aantal inwoners die tevreden zijn met hun sociale leven en het totale aantal inwoners werden vervolgens gebruikt om terug te rekenen naar het percentage inwoners die tevreden zijn met hun sociale leven.
    """,
    "Aantal ondervonden delicten": """
        **Welkom bij Aantal ondervonden delicten indicator**
        - Deze indicator is onderdeel van het Veiligheid thema.
        - Meeteenheid: aantal misdrijven per 100 inwoners
        - Voor deze indicator kan geen specifieke ruimtelijke spillover-/compensatieafstand worden aangenomen, omdat hierover geen relevante literatuur beschikbaar is. Daarom wordt in deze analyse een eerste-orde-contiguïteit (first order contiguity) toegepast. Dit betekent dat aangenomen wordt dat wanneer gemeenten een grens delen, het aantal misdrijven dat wordt ervaren over deze grenzen heen overloopt. De gemiddelde waarde voor het aantal misdrijven dat wordt ervaren per gemeente wordt verstrekt door het CBS, als aantal per 100 inwoners.
        - Om rekening te houden met de bevolkingsgrootte van elke gemeente, moest de waarde die door het CBS werd verstrekt, worden gedeeld door 100 en vervolgens worden vermenigvuldigd met het inwoneraantal van elke gemeente. Dit aantal is gebruikt in de verdere berekeningen.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over het aantal misdrijven dat wordt ervaren geanalyseerd met behulp van ArcGIS Pro. De Neighborhood Summary Statistics Tool is op deze gegevens toegepast. Deze tool berekent, op basis van de eerste-orde-contiguïteitsgrenzen, de waarden van alle aangrenzende gemeenten en de gemeente zelf om een gemiddelde waarde te berekenen. Het past de oorspronkelijke waarde aan om het ruimtelijke spillover effect over gemeentelijke grenzen heen te compenseren.
        - De berekende gemiddelde waarde wordt vervolgens gedeeld door het inwoneraantal en vermenigvuldigd met 100 om terug te rekenen naar het aantal misdrijven dat wordt ervaren per 100 inwoners.
    """,
    "Geregistreerde misdrijven": """
        **Welkom bij Geregistreerde misdrijven indicator**
        - Deze indicator is onderdeel van het Veiligheid thema.
        - 2021 en 2022 zijn voorlopige cijfers
        - Meeteenheid: geregistreerde misdaden per 1000 inwoners
        - Voor deze indicator kan geen specifieke ruimtelijke spillover-/compensatieafstand worden aangenomen, omdat hierover geen relevante literatuur beschikbaar is. Daarom wordt in deze analyse een eerste-orde-contiguïteit (first order contiguity) toegepast. Dit betekent dat aangenomen wordt dat wanneer gemeenten een grens delen, geregistreerde misdrijven over deze grenzen heen overlopen. De gemiddelde waarde voor geregistreerde misdrijven per gemeente wordt verstrekt door het CBS, als aantal per 1000 inwoners.
        - Om rekening te houden met de bevolkingsgrootte van elke gemeente, moest de waarde die door het CBS werd verstrekt, worden gedeeld door 1000 en vervolgens worden vermenigvuldigd met het inwoneraantal van elke gemeente. Dit aantal is gebruikt in de verdere berekeningen.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over geregistreerde misdrijven geanalyseerd met behulp van ArcGIS Pro. De Neighborhood Summary Statistics Tool is op deze gegevens toegepast. Deze tool berekent, op basis van de eerste-orde-contiguïteitsgrenzen, de waarden van alle aangrenzende gemeenten en de gemeente zelf om een gemiddelde waarde te berekenen. Het past de oorspronkelijke waarde aan om het ruimtelijke spillover effect over gemeentelijke grenzen heen te compenseren.
        - De berekende gemiddelde waarde wordt vervolgens gedeeld door het inwoneraantal en vermenigvuldigd met 1000 om terug te rekenen naar geregistreerde misdrijven per 1000 inwoners.
    """,
    "Natuurgebied per inwoner": """
        **Welkom bij Natuurgebied per inwoner indicator**
        - Deze indicator is onderdeel van het Milieu thema
        - Meeteenheid: ha per 1000 inwoners
        - Voor deze indicator wordt uitgegaan van een ruimtelijke spillover-/compensatieafstand van 1650 meter. Dit houdt in dat aangenomen wordt dat mensen gemiddeld bereid zijn om 1650 meter af te leggen naar natuurgebieden. De gemiddelde waarde voor natuurgebieden per gemeente wordt gegeven door het CBS, als een waarde per 1000 inwoners.
        - Om rekening te houden met het totale natuurgebied in elke gemeente, moet de waarde per 1000 inwoners worden omgerekend naar het totale natuurgebied per gemeente, door de waarde te delen door 1000 en te vermenigvuldigen met het totale aantal inwoners. Dit aantal is gebruikt in de verdere berekeningen.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over natuurgebieden geanalyseerd met behulp van ArcGIS Pro. Eerst zijn de gemeentelijke polygonen (met gegevens over natuurgebieden) omgezet in rastercellen van 100x100 meter. Elke rastercel kreeg de waarde van het bijbehorende gemeentelijke polygoon. Vervolgens werden focale statistieken toegepast om de gemiddelde waarde voor elke rastercel te berekenen op basis van de omliggende cellen. Door een cirkelvormige neighborhood met een straal van 1650 meter te gebruiken, wordt een gemiddelde berekend van alle waarden van rastercellen binnen deze straal, zodat het spillover effect van natuurgebieden en de invloed van nabijgelegen gemeenten wordt meegenomen.
        - Door gebruik te maken van zone-statistieken worden de geüpdatete rastercellen samengevat naar de gemeentelijke polygonen. Voor elk gemeentelijk polygoon werd de gemiddelde waarde berekend van alle rastercellen die binnen de grenzen van het polygoon vallen. Dit resulteert in één waarde voor natuurgebieden per gemeente, waarbij rekening wordt gehouden met reizen over gemeentegrenzen heen. Deze waarde werd vervolgens gedeeld door de totale bevolking en vermenigvuldigd met 1000.
    """,
    "Levensverwachting van de bevolking": """
        **Welkom bij Levensverwachting van de bevolking indicator**
        - Deze indicator is onderdeel van het Gezondheid thema
        - Voor deze indicator kan geen specifieke ruimtelijke spillover-/compensatieafstand worden aangenomen, omdat hierover geen relevante literatuur beschikbaar is. Daarom wordt in deze analyse een eerste-orde-contiguïteit (first order contiguity) toegepast. Dit betekent dat aangenomen wordt dat de levensverwachting van de bevolking overloopt naar aangrenzende gemeenten. De gemiddelde waarde voor de levensverwachting van de bevolking per gemeente wordt gegeven door het CBS.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over de levensverwachting van de bevolking geanalyseerd met behulp van ArcGIS Pro. De neighborhood summary statistics tool is toegepast op deze gegevens. Deze tool berekent, op basis van eerste-orde-contiguïteitsgrenzen, de gemiddelde waarde van alle aangrenzende gemeenten en de gemeente zelf. Het past de oorspronkelijke waarde aan om rekening te houden met het ruimtelijke spillover-effect over gemeentegrenzen heen.
    """,
    "Emissies van fijnstof naar lucht": """
        **Welkom bij Emissies van fijnstof naar lucht indicator**
        - Deze indicator is onderdeel van het Milieu thema
        - Meeteenheid: microgram PM 2,5 per m^3
        - Voor deze indicator wordt uitgegaan van een ruimtelijke spillover-/compensatieafstand van 500 meter. Dit betekent dat er wordt uitgegaan van het feit dat emissies van fijnstof naar de lucht gemiddeld gezien zich verspreiden tot 500 meter van elke locatie, wat de invloed van nabijgelegen gebieden weergeeft. De gemiddelde emissie van fijnstof naar de lucht per gemeente wordt gegeven door het CBS, als kg PM₂.₅ per km².
        - Om rekening te houden met de oppervlakte van elke gemeente, moest de door het CBS verstrekte waarde worden vermenigvuldigd met de totale oppervlakte (in km²) van elke gemeente. Dit aantal is gebruikt in de verdere berekeningen.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over emissies van fijnstof naar de lucht geanalyseerd met behulp van ArcGIS Pro. Eerst zijn de gemeentelijke polygonen (met gegevens over emissies van fijnstof in de lucht) omgezet in rastercellen van 100x100 meter. Elke rastercel kreeg de waarde van het bijbehorende gemeentelijke polygoon. Vervolgens werden focale statistieken toegepast om de gemiddelde waarde voor elke rastercel te berekenen op basis van de omliggende cellen. Door een cirkelvormige neighborhood met een straal van 500 meter te gebruiken, wordt een gemiddelde berekend van alle waarden van rastercellen binnen deze straal, zodat het spillover effect van emissies van fijnstof naar de lucht en de invloed van nabijgelegen gemeenten wordt meegenomen.
        - Door gebruik te maken van zone-statistieken worden de geüpdatete rastercellen samengevat naar de gemeentelijke polygonen. Voor elk gemeentelijk polygoon werd de gemiddelde waarde berekend van alle rastercellen die binnen de grenzen van het polygoon vallen. Dit resulteert in één waarde voor emissies van fijnstof in de lucht per gemeente, waarbij rekening is gehouden met het ruimtelijke spillover-effect over gemeentegrenzen. Deze waarde werd vervolgens gedeeld door de totale oppervlakte (in km²) van elke gemeente.
    """,
    "Afstand tot openbaar groen": """
        **Welkom bij Afstand tot openbaar groen indicator**
        - Deze indicator is onderdeel van het Milieu thema
        - Meeteenheid: Kilometers
        - Voor deze indicator wordt er gewerkt met een ruimtelijke spillover-/compensatieafstand van 1650 meter. Dit betekent dat er wordt uitgegaan van het feit dat men gemiddeld bereid is om 1650 meter te reizen voor toegang tot openbaar groen. De gemiddelde afstanden tot openbaar groen per gemeente zijn gegeven door het CBS.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over de gemiddelde afstanden tot openbaar groen geanalyseerd met behulp van ArcGIS Pro. Eerst zijn de gemeentelijke polygonen (met gegevens over de afstand tot café’s enz.) omgezet in rastercellen van 100x100 meter. Elke rastercel kreeg de waarde van het bijbehorende gemeentelijke polygoon. Vervolgens zijn focale statistieken toegepast om de gemiddelde waarde voor elke rastercel te berekenen op basis van de omliggende cellen. Door een cirkelvormige neighborhood met een straal van 1650 meter te gebruiken, wordt een gemiddelde berekend van alle waarden van rastercellen binnen deze straal, zodat het spillover effect van afstanden tot openbaar groen en de invloed van nabijgelegen gemeenten wordt meegenomen.
        - Met behulp van zone-statistieken zijn de geüpdatete rastercellen terug gerekend naar de gemeentelijke polygonen. Voor elk gemeentelijk polygoon is de gemiddelde waarde van alle rastercellen binnen de grenzen berekend. Dit resulteert in één waarde voor de afstand tot openbaar groen per gemeente, waarbij rekening wordt gehouden met reizen over gemeentegrenzen.
        - Ten slotte, als de berekende ruimtelijke spillover afstand groter is dan de oorspronkelijke waarde, blijft de oorspronkelijke waarde behouden. Dit betekent dat de oorspronkelijke waarde alleen wordt bijgewerkt wanneer er een compenserende ruimtelijke spillover tussen gemeenten is, ervan uitgaande dat individuen niet verder reizen naar een aangrenzende gemeente als de voorziening dichterbij beschikbaar is in hun eigen woonplaats.

    """,
    "Broeikasgasemissies per inwoner": """
        **Welkom bij Broeikasgasemissies per inwoner indicator**
        - Deze indicator is onderdeel van het Milieu thema
        - De gehele reeks is aangepast vanwege de nieuwe IPCC voorschriften.
        - Meeteenheid: Tonnen CO2-equivalent per inwoner
        - Voor deze indicator kan geen specifieke ruimtelijke spillover-/compensatieafstand worden aangenomen, omdat hierover geen relevante literatuur beschikbaar is. Daarom wordt in deze analyse een eerste-orde-contiguïteit (first order contiguity) toegepast. Dit betekent dat aangenomen wordt dat wanneer gemeenten een grens delen, broeikasgasemissies per inwoner over deze grenzen heen overlopen. De gemiddelde waarde voor broeikasgasemissies per inwoner per gemeente wordt verstrekt door het CBS.
        - Om rekening te houden met de bevolkingsgrootte van elke gemeente, moest de waarde die door het CBS werd verstrekt, worden vermenigvuldigd met het aantal inwoners van elke gemeente. Dit aantal is gebruikt in de verdere berekeningen.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over broeikasgasemissies per inwoner geanalyseerd met behulp van ArcGIS Pro. De Neighborhood Summary Statistics Tool is op deze gegevens toegepast. Deze tool berekent, op basis van de eerste-orde-contiguïteitsgrenzen, de waarden van alle aangrenzende gemeenten en de gemeente zelf om een gemiddelde waarde te berekenen. Het past de oorspronkelijke waarde aan om het ruimtelijke spillover effect over gemeentelijke grenzen heen te compenseren.
        - De berekende gemiddelde waarde wordt vervolgens gedeeld door het inwoneraantal om terug te rekenen naar de broeikasgasemissies per inwoner.
    """,
    "Kwaliteit van zwemwater binnenwateren": """
        **Welkom bij Kwaliteit van zwemwater binnenwateren indicator**
        - Deze indicator is onderdeel van het Milieu thema
        - Meeteenheid: Gemiddelde kwaliteit (1=slecht tot 4=uitstekend)
        - Voor deze indicator wordt er gewerkt met een ruimtelijke spillover-/compensatieafstand van 1650 meter. Dit betekent dat er wordt uitgegaan van het feit dat men gemiddeld bereid is om 1650 meter te reizen voor toegang tot binnenwateren voor zwemmen. Dit houdt in dat de kwaliteit van het water ook een spillover afstand van 1650 meter heeft. De gemiddelde kwaliteit van binnenwateren voor zwemmen per gemeente is gegeven door het CBS.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over de kwaliteit van binnenwateren voor zwemmen geanalyseerd met behulp van ArcGIS Pro. Eerst zijn de gemeentelijke polygonen (met gegevens over de kwaliteit van binnenwateren voor zwemmen) omgezet in rastercellen van 100x100 meter. Elke rastercel kreeg de waarde van het bijbehorende gemeentelijke polygoon. Vervolgens zijn focale statistieken toegepast om de gemiddelde waarde voor elke rastercel te berekenen op basis van de omliggende cellen. Door een cirkelvormige neighborhood met een straal van 1650 meter te gebruiken, wordt een gemiddelde berekend van alle waarden van rastercellen binnen deze straal, zodat het spillover effect van kwaliteit van zwemwater binnenwateren en de invloed van nabijgelegen gemeenten wordt meegenomen.
        - Met behulp van zone-statistieken zijn de geüpdatete rastercellen terug gerekend naar de gemeentelijke polygonen. Voor elk gemeentelijk polygoon is de gemiddelde waarde van alle rastercellen binnen de grenzen berekend. Dit resulteert in één waarde voor de kwaliteit van binnenwateren voor zwemmen per gemeente, waarbij rekening wordt gehouden met reizen over gemeentegrenzen.

    """,
    "Kwaliteit van zwemwater kustwateren": """
        **Welkom bij Kwaliteit van zwemwater kustwateren indicator**
        - Deze indicator is onderdeel van het Milieu thema
        - Meeteenheid: Gemiddelde kwaliteit (1=slecht tot 4=uitstekend)
        - Voor deze indicator wordt er gewerkt met een ruimtelijke spillover-/compensatieafstand van 1650 meter. Dit betekent dat er wordt uitgegaan van het feit dat men gemiddeld bereid is om 1650 meter te reizen voor toegang tot zwemwater in kustwateren. Dit houdt in dat de kwaliteit van het water ook een spilloverafstand van 1650 meter heeft. De gemiddelde kwaliteit van zwemwater in kustwateren per gemeente is gegeven door het CBS.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over de kwaliteit van zwemwater in kustwateren geanalyseerd met behulp van ArcGIS Pro. Eerst zijn de gemeentelijke polygonen (met gegevens over de kwaliteit van binnenwateren voor zwemmen) omgezet in rastercellen van 100x100 meter. Elke rastercel kreeg de waarde van het bijbehorende gemeentelijke polygoon. Vervolgens zijn focale statistieken toegepast om de gemiddelde waarde voor elke rastercel te berekenen op basis van de omliggende cellen. Door een cirkelvormige neighborhood met een straal van 1650 meter te gebruiken, wordt een gemiddelde berekend van alle waarden van rastercellen binnen deze straal, zodat het spillover effect van kwaliteit van zwemwater in kustwateren en de invloed van nabijgelegen gemeenten wordt meegenomen.
        - Met behulp van zone-statistieken zijn de geüpdatete rastercellen terug gerekend naar de gemeentelijke polygonen. Voor elk gemeentelijk polygoon is de gemiddelde waarde van alle rastercellen binnen de grenzen berekend. Dit resulteert in één waarde voor de kwaliteit van zwemwater in kustwateren per gemeente, waarbij rekening wordt gehouden met reizen over gemeentegrenzen.

    """,
    "Gemiddelde schuld per huishouden": """
        **Welkom bij Gemiddelde schuld per huishouden indicator**
        - Deze indicator is onderdeel van het Economisch kapitaal
        - 2022 zijn voorlopige cijfers en de correctie voor de prijsverandering in 2021 en 2022 is gebaseerd op de onderzoeksreeks consumentenprijzen, die de daadwerkelijk betaalde energieprijzen gebruikt. Deze sluit gemiddeld genomen meer aan bij de prijsontwikkeling die de bevolking heeft ervaren dan de consumentenprijsindex.
        - Meeteenheid: Gemiddelde schuld per huishouden in euro
        - Voor deze indicator kan geen specifieke ruimtelijke spillover-/compensatieafstand worden aangenomen, omdat hierover geen relevante literatuur beschikbaar is. Daarom wordt in deze analyse een eerste-orde-contiguïteit (first order contiguity) toegepast. Dit betekent dat aangenomen wordt dat wanneer gemeenten een grens delen, de gemiddelde schuld per huishouden over deze grenzen heen overloopt. De gemiddelde waarde voor de gemiddelde schuld per huishouden per gemeente wordt gegeven door het CBS.
        - Om rekening te houden met de grootte van elke gemeente, moest de waarde van de gemiddelde schuld per huishouden worden vermenigvuldigd met het aantal huishoudens van de gemeente. Dit aantal is gebruikt in de verdere berekeningen.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over de gemiddelde schuld per huishouden geanalyseerd met behulp van ArcGIS Pro. Eerst werden aangrenzende gemeenten bepaald op basis van gedeelde grenzen, gedefinieerd als geometrieën die elkaar raken. Vervolgens werden voor elke gemeente twee variabelen geactiveerd: één om het totale aantal huishoudens van de gemeente en haar aangrenzende gemeenten op te tellen, en een andere om de totale schuld van alle huishoudens in de gemeente en haar aangrenzende gemeenten op te tellen. Het doel is om een gecombineerde score te berekenen door ook de aangrenzende gemeenten mee te nemen.
        - Het berekende totale schuldbedrag en het totale aantal huishoudens werden vervolgens gebruikt om terug te rekenen naar de gemiddelde schuld per huishouden.
    """,
    "Mediaan vermogen van huishoudens": """
        **Welkom bij Mediaan vermogen van huishoudens indicator**
        - Deze indicator is onderdeel van het Economisch kapitaal
        - 2021 zijn voorlopige cijfers en de correctie voor de prijsverandering in 2021 is gebaseerd op de onderzoeksreeks consumentenprijzen, die de daadwerkelijk betaalde energieprijzen gebruikt. Deze sluit gemiddeld genomen meer aan bij de prijsontwikkeling die de bevolking heeft ervaren dan de consumentenprijsindex.
        - Meeteenheid: Euro
        - Voor deze indicator kan geen specifieke ruimtelijke spillover-/compensatieafstand worden aangenomen, omdat hierover geen relevante literatuur beschikbaar is. Daarom wordt in deze analyse een eerste-orde-contiguïteit (first order contiguity) toegepast. Dit betekent dat aangenomen wordt dat wanneer gemeenten een grens delen, het mediaan huishoudvermogen over deze grenzen heen overloopt. De gemiddelde waarde voor het mediaan huishoudvermogen per gemeente wordt gegeven door het CBS.
        - Om rekening te houden met de grootte van elke gemeente, moest de waarde van het mediaan huishoudvermogen worden vermenigvuldigd met het aantal huishoudens van de gemeente. Dit aantal is gebruikt in de verdere berekeningen.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over het mediaan huishoudvermogen geanalyseerd met behulp van ArcGIS Pro. Eerst werden aangrenzende gemeenten bepaald op basis van gedeelde grenzen, gedefinieerd als geometrieën die elkaar raken. Vervolgens werden voor elke gemeente twee variabelen geactiveerd: één om het totale aantal huishoudens van de gemeente en haar aangrenzende gemeenten op te tellen, en een andere om het totale vermogen van alle huishoudens in de gemeente en haar aangrenzende gemeenten op te tellen. Het doel is om een gecombineerde score te berekenen door ook de aangrenzende gemeenten mee te nemen.
        - Het berekende totale vermogen en het totale aantal huishoudens werden vervolgens gebruikt om terug te rekenen naar het mediaan huishoudvermogen.
    """,
    "Particuliere zonne-energie": """
        **Welkom bij Particuliere zonne-energie indicator**
        - Deze indicator is onderdeel van het Natuurlijk kapitaal
        - cijfers 2021 en 2022 zijn voorlopig
        - Meeteenheid: Watt per huis
        - Voor deze indicator wordt uitgegaan van een ruimtelijke spillover-/compensatieafstand van 1 km. Dit betekent dat er wordt uitgegaan van het feit dat particuliere zonne-energie gemiddeld gezien zich uitstrekt tot 1 km van elke locatie, wat de invloed van nabijgelegen gebieden weerspiegelt. De gemiddelde waarde voor particuliere zonne-energie per gemeente wordt gegeven door het CBS, als een gemiddelde waarde in watt per woning.
        - Om rekening te houden met het aantal woningen in elke gemeente, werd de gemiddelde waarde in watt per woning omgerekend naar het totale aantal watt aan particuliere zonne-energie per gemeente, door vermenigvuldiging met het aantal woningen in elke gemeente. Dit aantal is gebruikt in de verdere berekeningen.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over particuliere zonne-energie geanalyseerd met behulp van ArcGIS Pro. Eerst zijn de gemeentelijke polygonen (met gegevens over particuliere zonne-energie) omgezet in rastercellen van 100x100 meter. Elke rastercel kreeg de waarde van het bijbehorende gemeentelijke polygoon. Vervolgens werden focale statistieken toegepast om de gemiddelde waarde voor elke rastercel te berekenen op basis van de omliggende cellen. Door een cirkelvormige neighborhood met een straal van 1 km te gebruiken, wordt een gemiddelde berekend van alle waarden van rastercellen binnen deze straal, zodat het spillover effect van particuliere zonne-energie en de invloed van nabijgelegen gemeenten wordt meegenomen.
        - Door gebruik te maken van zone-statistieken worden de geüpdatete rastercellen samengevat naar de gemeentelijke polygonen. Voor elk gemeentelijk polygoon werd de gemiddelde waarde berekend van alle rastercellen die binnen de grenzen van het polygoon vallen. Dit resulteert in één waarde voor particuliere zonne-energie per gemeente, waarbij rekening is gehouden met het ruimtelijke spillover-effect over gemeentegrenzen. Deze waarde werd vervolgens gedeeld door het totale aantal woningen in elke gemeente.
    """,
    "Natuur- en bosgebieden": """
        **Welkom bij Natuur- en bosgebieden indicator**
        - Deze indicator is onderdeel van het Natuurlijk kapitaal
        - Meeteenheid: Percentage van het landoppervlak
        - Voor deze indicator wordt gewerkt met een ruimtelijke spillover-/compensatieafstand van 1650 meter. Dit betekent dat er wordt uitgegaan van het feit dat individuen gemiddeld gezien bereid zijn om 1650 meter af te leggen voor toegang tot natuur- en bosgebieden. De gemiddelde waarde voor natuur- en bosgebieden per gemeente wordt gegeven door het CBS, als een percentage van de oppervlakte.
        - Om rekening te houden met de oppervlakte van elke gemeente, is het percentage van natuur- en bosoppervlak omgezet in een werkelijke oppervlakte waarde. Deze waarde is gebruikt in de verdere berekeningen.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over natuur- en bosgebieden geanalyseerd met behulp van ArcGIS Pro. Eerst zijn de gemeentelijke polygonen (met gegevens over natuur- en bosgebieden) omgezet in rastercellen van 100x100 meter. Dit werd gedaan door twee aparte rasterlagen te maken: een die de natuur- en bosoppervlakte representeert, en de andere die de totale oppervlakte representeert. Voor beide rasterlagen kreeg elke rastercel de waarde van het bijbehorende gemeentelijke polygoon.
        - Vervolgens werden focale statistieken toegepast op beide rasterlagen afzonderlijk. Dit gebeurde door de gemiddelde waarde voor elke rastercel te berekenen op basis van de omliggende cellen. Door een cirkelvormige neighborhood met een straal van 1650 meter te gebruiken, wordt een gemiddelde berekend van alle waarden van rastercellen binnen deze straal, zodat het spillover effect van natuur- en bosgebieden en de invloed van nabijgelegen gemeenten wordt meegenomen.
        - Door gebruik te maken van zone-statistieken worden de geüpdatete rastercellen samengevat naar de gemeentelijke polygonen voor beide rasterlagen. Voor elk gemeentelijk polygoon werd de gemiddelde waarde berekend van alle rastercellen die binnen de grenzen van het polygoon vallen. Dit werd gedaan voor zowel de natuur- en bosoppervlakte, als voor de totale oppervlakte. Deze twee waarden werden vervolgens gebruikt om het percentage van de natuur- en bosoppervlakte opnieuw te berekenen, aangepast voor het ruimtelijke spillover-effect over gemeentegrenzen.
    """,
    "Bebouwd terrein": """
        **Welkom bij Bebouwd terrein indicator**
        - Deze indicator is onderdeel van het Natuurlijk kapitaal
        - Meeteenheid: Percentage van het landoppervlak
        - Voor deze indicator kan geen specifieke ruimtelijke spillover-/compensatieafstand worden aangenomen, omdat hierover geen relevante literatuur beschikbaar is. Daarom wordt in deze analyse een eerste-orde-contiguïteit (first order contiguity) toegepast. Dit betekent dat aangenomen wordt dat wanneer gemeenten een grens delen, een bebouwd terrein over deze grenzen heen overloopt. De gemiddelde waarde voor bebouwd terrein per gemeente wordt gegeven door het CBS, als percentage van de oppervlakte die is bebouwd.
        - Om rekening te houden met de grootte van elke gemeente, moest het percentage van het bebouwd terrein worden omgezet naar een werkelijk oppervlakte waarde. Dit aantal is gebruikt in de verdere berekeningen.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over bebouwd terrein geanalyseerd met behulp van ArcGIS Pro. Eerst werden aangrenzende gemeenten bepaald op basis van gedeelde grenzen, gedefinieerd als geometrieën die elkaar raken. Vervolgens werden voor elke gemeente twee variabelen geactiveerd: één om de oppervlakte van de gemeente en haar aangrenzende gemeenten dat bebouwd is op te tellen, en een andere om het totale oppervlak van de gemeente en haar aangrenzende gemeenten op te tellen. Het doel is om een gecombineerde score te berekenen door ook de aangrenzende gemeenten mee te nemen.
        - Het berekende totale aantal bebouwd terrein en het totale oppervlak werden vervolgens gebruikt om terug te rekenen naar het percentage bebouwd terrein.
    """,
    "Sociale cohesie": """
        **Welkom bij Sociale cohesie indicator**
        - Deze indicator is onderdeel van het Sociaal kapitaal
        - Meeteenheid: schaalscore (0-10)
        - Voor deze indicator kan geen specifieke ruimtelijke spillover-/compensatieafstand worden aangenomen, omdat hierover geen relevante literatuur beschikbaar is. Daarom wordt in deze analyse een eerste-orde-contiguïteit (first order contiguity) toegepast. Dit betekent dat aangenomen wordt dat wanneer gemeenten een grens delen, sociale cohesie over deze grenzen heen overloopt. De gemiddelde waarde voor sociale cohesie per gemeente wordt gegeven door het CBS.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over sociale cohesie geanalyseerd met behulp van ArcGIS Pro. De neighborhood summary statistics tool is toegepast op deze gegevens. Deze tool berekent, op basis van eerste-orde-contiguïteitsgrenzen, de waarden van alle aangrenzende gemeenten en de gemeente zelf, om een gemiddelde waarde te berekenen. Het past de oorspronkelijke waarde aan om rekening te houden met het ruimtelijke spillover-effect over gemeentegrenzen heen.

    """,
    "Geregisteerde problematische schulden": """
        **Welkom bij Geregisteerde problematische schulden indicator**
        - Deze indicator is onderdeel van het Sociaal kapitaal
        - Meeteenheid: schaalscore (0-10)
        - Voor deze indicator kan geen specifieke ruimtelijke spillover-/compensatieafstand worden aangenomen, omdat hierover geen relevante literatuur beschikbaar is. Daarom wordt in deze analyse een eerste-orde-contiguïteit (first order contiguity) toegepast. Dit betekent dat aangenomen wordt dat wanneer gemeenten een grens delen, geregistreerde problematische schulden over deze grenzen heen overlopen. De gemiddelde waarde voor geregistreerde problematische schulden per gemeente wordt gegeven door het CBS, als percentage van de huishoudens die geregistreerde problematische schulden hebben.
        - Om rekening te houden met de bevolkingsgrootte van elke gemeente, moest het percentage van de huishoudens die geregistreerde problematische schulden hebben, worden omgezet naar het totale aantal huishoudens die geregistreerde problematische schulden hebben. Dit aantal is gebruikt in de verdere berekeningen.
        - Om gemeentelijke spillovers in kaart te brengen, zijn de CBS-gegevens over geregistreerde problematische schulden geanalyseerd met behulp van ArcGIS Pro. Eerst werden aangrenzende gemeenten bepaald op basis van gedeelde grenzen, gedefinieerd als geometrieën die elkaar raken. Vervolgens werden voor elke gemeente twee variabelen geactiveerd: één om de huishoudens van de gemeente en haar aangrenzende gemeenten die geregistreerde problematische schulden hebben op te tellen, en een andere om het totale aantal huishoudens van de gemeente en haar aangrenzende gemeenten op te tellen. Het doel is om een gecombineerde score te berekenen door ook de aangrenzende gemeenten mee te nemen.
        - Het berekende totale aantal huishoudens die geregistreerde problematische schulden hebben en het totale aantal huishoudens werden vervolgens gebruikt om terug te rekenen naar het percentage huishoudens die geregistreerde problematische schulden hebben.
    """,

    # Themes 

    "Gezondheid": """
        **Welkom bij het thema Gezondheid**
        - In dit thema zijn de volgende indicatoren opgenomen: Overgewicht, Ervaren gezondheid, Levensverwachting van de bevolking, Mensen met een of meer langdurige ziekten of aandoeningen
        - Het thema **gezondheid** bestaat uit de indicatoren **overgewicht**, **ervaren gezondheid** en **mensen met een of meer langdurige ziekten of aandoeningen**.  
        - Zoals gedefinieerd door het CBS, is de indicator **overgewicht** het percentage personen van 18 jaar en ouder met een BMI van 25,0 kg/m² of hoger. Het lichaamsgewicht is gebaseerd op zelfgerapporteerde waarden. De Body Mass Index (BMI) is een maat voor overgewicht en wordt berekend als het gewicht in kilogrammen gedeeld door het kwadraat van de lengte in meters (kg/m²).  
        - Zoals gedefinieerd door het CBS, is de indicator **ervaren gezondheid** het percentage personen van 18 jaar en ouder dat hun algemene gezondheidstoestand als ‘goed’ of ‘zeer goed’ beoordeelt.  

        - Zoals gedefinieerd door het CBS, is de indicator **mensen met een of meer langdurige ziekten of aandoeningen** het percentage personen van 18 jaar en ouder met een of meer langdurige ziekten of aandoeningen. Langdurig betekent (naar verwachting) 6 maanden of langer.  

        - De indicator **levensverwachting van de bevolking** (levensverwachting bij geboorte, gemiddeld over de periode 2019-2022) is niet opgenomen in dit thema. Aangezien vergelijking en ontwikkeling door de jaren heen relevanter zijn voor het onderzoek dan een momentopname van één jaar, is ervoor gekozen deze indicator niet mee te nemen.  

        - Beschikbare gegevens per indicator:  
        - **Overgewicht**: 2016, 2020 en 2022  
        - **Ervaren gezondheid**: 2016, 2020 en 2022  
        - **Mensen met een of meer langdurige ziekten of aandoeningen**: 2016, 2020 en 2022  

        - Het thema **gezondheid** bestaat daarmee uit de indicatoren **overgewicht**, **ervaren gezondheid** en **mensen met een of meer langdurige ziekten of aandoeningen** voor de jaren 2016, 2020 en 2022.
    """,
    "Subjectief welzijn": """
        **Welkom bij het thema Welzijn**
        - In dit thema zijn de volgende indicatoren opgenomen: Tevredenheid met het leven, Tevredenheid met vrije tijd
        - Het thema welzijn bestaat uit de indicatoren tevredenheid met vrije tijd en tevredenheid met het leven.
        - Zoals gedefinieerd door het CBS, is tevredenheid met vrije tijd en tevredenheid met het leven het percentage van de personen van 18 jaar en ouder die een score tussen 7 en 10 geven op de vraag: "Kun je op een schaal van 1 tot 10 aangeven in hoeverre je tevreden bent met de hoeveelheid vrije tijd die je hebt? Een score van 1 staat voor volledig ontevreden en een score van 10 voor volledig tevreden?". Een score van 7 tot 10 wordt als tevreden beschouwd.
        - Voor beide indicatoren zijn de jaren 2013-2023 aanwezig in de dataset en zijn beide volledig opgenomen in de score voor het thema welzijn.
    """,
    "Materiale welvaart": """
        **Welkom bij het thema Materieel Welzijn en Economisch Kapitaal**
        - In dit thema zijn de volgende indicatoren opgenomen: Mediaan besteedbaar inkomen, Bruto binnenlands product, Gemiddelde schuld per huishouden, Mediaan huishoudvermogen
        - Het thema **materiële welvaart en economische voorspoed** bestaat uit de indicatoren **mediaan besteedbaar inkomen**, **gemiddelde schuld per huishouden**, **mediaan vermogen van huishoudens** en **gemiddelde problematische schuld**.  

        - Zoals gedefinieerd door het CBS, is de indicator **mediaan besteedbaar inkomen** het gestandaardiseerde mediaan besteedbaar inkomen per huishouden in euro’s. Bij de berekening wordt gecorrigeerd voor verschillen in grootte en samenstelling van huishoudens. De mediaan is de middelste waarde wanneer alle inkomens van laag naar hoog zijn gerangschikt.  

        - Zoals gedefinieerd door het CBS, is de indicator **gemiddelde schuld per huishouden** het gemiddelde van de schulden van particuliere huishoudens in het betreffende jaar. De schulden omvatten de hypotheek op de eigen woning, studieschuld, andere schulden zoals voor consumptieve doeleinden, financiering van aandelen, obligaties of recht op periodieke uitkeringen, schulden voor de financiering van een tweede woning of ander onroerend goed. Bedrag per 1 januari, gecorrigeerd voor prijsontwikkelingen in het voorgaande jaar.  

        - Zoals gedefinieerd door het CBS, is de indicator **mediaan vermogen van huishoudens** het saldo van bezittingen en schulden, gecorrigeerd voor inflatie, in prijzen van 2023. Bezittingen bestaan uit bank- en spaartegoeden, effecten, de eigen woning, ander onroerend goed, ondernemingsvermogen, aanmerkelijk belang en overige bezittingen. Schulden omvatten de hypotheekschuld van de eigen woning en consumptief krediet. Positie per 1 januari, gecorrigeerd voor prijsontwikkelingen in het voorgaande jaar.  

        - Zoals gedefinieerd door het CBS, is de indicator **gemiddelde problematische schuld** het percentage huishoudens met geregistreerde problematische schulden op 1 januari van het betreffende jaar. De populatie bestaat uit alle particuliere huishoudens in Nederland die op 1 januari van het referentiejaar in de BRP (Basisregistratie Personen) waren geregistreerd. Aan de hand van verschillende registraties is bepaald welke huishoudens geregistreerde problematische schulden hebben. De beschikbare informatie over schulden verschilt per registratie, waardoor per registratie is bepaald of en wanneer sprake is van een geregistreerde problematische schuldensituatie.  

        - Beschikbare gegevens per indicator:  
        - **Mediaan besteedbaar inkomen**: 2013-2023  
        - **Gemiddelde schuld per huishouden**: 2013-2023  
        - **Mediaan vermogen van huishoudens**: 2013-2023  
        - **Gemiddelde problematische schuld**: 2021-2023  
        - Het thema **materiële welvaart en economische voorspoed** is daarmee geconstrueerd voor de jaren 2021 tot en met 2023.
    """,
    "Arbeid en vrije tijd": """
        **Welkom bij het thema Arbeid en Vrije Tijd**
        - In dit thema zijn de volgende indicatoren opgenomen: Netto arbeidsparticipatie, Bruto arbeidsparticipatie, Hoogopgeleide bevolking, Werkloosheid, Vacaturepercentage
        - Het thema **arbeid en vrije tijd** bestaat uit de indicatoren **netto arbeidsparticipatie**, **hoogopgeleide bevolking (mensen met een startkwalificatie)**, **werkloosheid** en **afstand tot openbaar vervoer**.  

        - Zoals gedefinieerd door het CBS, is de indicator **netto arbeidsparticipatie** het aandeel van de werkzame beroepsbevolking van 15 tot 74 jaar binnen de totale bevolking van dezelfde leeftijdsgroep (werkzame en niet-werkzame bevolking).  

        - Zoals gedefinieerd door het CBS, is de indicator **hoogopgeleide bevolking (mensen met een startkwalificatie)** het percentage van de bevolking van 15 tot 74 jaar met een diploma op MBO 2, 3 of 4, HAVO, VWO, HBO of WO-niveau.  

        - Zoals gedefinieerd door het CBS, is de indicator **werkloosheid** de werkloze beroepsbevolking als percentage van de totale beroepsbevolking (werkzame en werkloze beroepsbevolking). Dit betreft personen van 15 tot 74 jaar zonder betaald werk, die recent naar werk hebben gezocht en direct beschikbaar zijn voor werk.  

        - Zoals gedefinieerd door het CBS, is de indicator **afstand tot openbaar vervoer** de gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde halte van het openbaar vervoer, berekend over het fietsroutenetwerk van 2023. Dit betreft de volgende vormen van openbaar vervoer: trein, tram, bus, metro en veerpont. De peildatum is 1 januari van het betreffende jaar.  

        - Beschikbare gegevens per indicator:  
        - **Netto arbeidsparticipatie**: 2013 tot en met 2023  
        - **Hoogopgeleide bevolking (mensen met een startkwalificatie)**: 2013 tot en met 2023  
        - **Werkloosheid**: 2013 tot en met 2023  
        - **Afstand tot openbaar vervoer**: 2017 tot en met 2023  

        Het thema **arbeid en vrije tijd** is geconstrueerd voor de jaren 2017 tot en met 2023.
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
        - Het CBS heeft een thema over veiligheid, maar door het ontbreken van gegevens voor een groot aantal gemeenten is het niet zinvol om een thematische kaart te maken voor een vergelijking over de jaren heen. Daarom is veiligheid geen thema binnen dit project.
    """,
    "Milieu": """
        **Welkom bij het thema Milieu**
        - In dit thema zijn de volgende indicatoren opgenomen: Oppervlakte natuurgebied per inwoner, Emissies van fijnstof naar de lucht, Natuur- en bosgebieden, Afstand tot openbaar groen, Uitstoot broeikasgassen per hoofd van de bevolking, Kwaliteit zwemwater in het binnenland, Kwaliteit zwemwater aan de kust
        - Het thema **milieu** bestaat uit de indicatoren **natuurgebied per inwoner**, **emissies van fijnstof naar de lucht**, **natuur- en bosgebieden**, **afstand tot openbaar groen** en **broeikasgasemissies per capita**.  
        - De indicatoren **kwaliteit van binnenlandse zwemwateren** en **kwaliteit van zwemwater in kustwateren** zijn niet opgenomen in het thema milieu, omdat deze indicatoren per definitie alleen worden gedefinieerd op locaties waar substantiële binnenwateren aanwezig zijn of in gemeenten aan de kust met kustwateren. Gegevens over gemeenten zonder deze kenmerken ontbreken. De discrepantie in beschikbare gegevens tussen deze indicatoren heeft geleid tot de beslissing om ze uit het thema milieu te laten.  
        - Zoals gedefinieerd door het CBS, is de indicator **natuurgebied per inwoner** de hoeveelheid hectares bos en open natuurlijk terrein per 1000 inwoners.  
        - **Bos**: terrein beplant met bomen, bedoeld voor houtproductie en/of natuurbeheer, inclusief onverharde en halfverharde wegen.  
        - **Natuurlijk terrein**: terrein in droge en natte natuurlijke staat.  
        - Zoals gedefinieerd door het CBS, is de indicator **emissies van fijnstof naar de lucht** de jaarlijkse gemiddelde fijnstofemissie naar de lucht. De fijnere fractie van fijnstof bestaat uit deeltjes met een diameter van minder dan 2,5 micrometer.  

        - Zoals gedefinieerd door het CBS, is de indicator **natuur- en bosgebieden** het percentage van het totale landoppervlak dat bestaat uit bos en open natuurlijk terrein.  
        - **Bos**: terrein beplant met bomen, bedoeld voor houtproductie en/of natuurbeheer, inclusief onverharde en halfverharde wegen.  
        - **Natuurlijk terrein**: terrein in droge en natte natuurlijke staat.  

        - Zoals gedefinieerd door het CBS, is de indicator **afstand tot openbaar groen** de gemiddelde afstand van alle inwoners in een gebied tot het dichtstbijzijnde openbare groen, berekend over de weg.  
        - **Openbaar groen** is land dat wordt gebruikt als park of openbare tuin, voor dagrecreatie, natuur of als bos. De grond kan zowel privé als openbaar toegankelijk zijn en heeft een minimale grootte van één hectare.  

        - Zoals gedefinieerd door het CBS, is de indicator **broeikasgasemissies per capita** de totale uitstoot van broeikasgassen (CO2, CH4, N2O, HFC, PFC en SF6) in CO2-equivalenten per inwoner. Eén kg CO2-equivalent komt overeen met het effect van de uitstoot van 1 kg koolstofdioxide (CO2). Bij de berekening van de CO2-equivalenten worden de richtlijnen van het IPCC gevolgd. De gegevens betreffen emissies op Nederlands grondgebied, ongeacht of deze worden veroorzaakt door Nederlandse inwoners. Dit betekent dat emissies door Nederlandse inwoners in het buitenland niet zijn inbegrepen, terwijl emissies door niet-ingezetenen in Nederland wel zijn opgenomen.  

        - Beschikbare gegevens per indicator:  
        - **Natuurgebied per inwoner**: 2015 en 2017  
        - **Emissies van fijnstof naar de lucht**: 2015 en 2019 tot en met 2022  
        - **Natuur- en bosgebieden**: 2015 en 2017  
        - **Afstand tot openbaar groen**: 2015 en 2017  
        - **Broeikasgasemissies per capita**: 2015 tot en met 2021  

        Het thema **milieu** is geconstrueerd voor het jaar 2015.
    """,
    "Luchtkwaliteit": """
        **Welkom bij het thema Luchtkwaliteit**
        - In dit thema zijn de volgende indicatoren opgenomen: Emissies van fijnstof naar de lucht, Broeikasgasemissies per hoofd van de bevolking
        - Het subthema luchtkwaliteit bestaat uit de indicatoren ‘emissies van fijnstof naar de lucht’ en ‘broeikasgasemissies per capita’.  
        - Zoals gedefinieerd door het CBS, is de indicator **emissies van fijnstof naar de lucht** de jaarlijkse gemiddelde fijnstofemissie naar de lucht. De fijnere fractie van fijnstof bestaat uit deeltjes met een diameter van minder dan 2,5 micrometer.  
        - Zoals gedefinieerd door het CBS, is de indicator **broeikasgasemissies per capita** de totale uitstoot van broeikasgassen (CO2, CH4, N2O, HFC, PFC en SF6) in CO2-equivalenten per inwoner. Eén kg CO2-equivalent komt overeen met het effect van de uitstoot van 1 kg koolstofdioxide (CO2). Bij de berekening van de CO2-equivalenten worden de richtlijnen van het IPCC gevolgd. De gegevens betreffen emissies op Nederlands grondgebied, ongeacht of deze worden veroorzaakt door Nederlandse inwoners. Dit betekent dat emissies door Nederlandse inwoners in het buitenland niet zijn inbegrepen, terwijl emissies door niet-ingezetenen in Nederland wel zijn opgenomen.  
        - De indicator **emissies van fijnstof naar de lucht** bevat gegevens voor de jaren 2015 en 2019 tot en met 2022.  
        - De indicator **broeikasgasemissies per capita** bevat gegevens voor de jaren 2015 tot en met 2021.  
        - Het subthema luchtkwaliteit is geconstrueerd voor de jaren 2019 tot en met 2021.
    """,
    "Natuurlijk kapitaal": """
        **Welkom bij het thema Natuurlijk Kapitaal**
        - In dit thema zijn de volgende indicatoren opgenomen: Particuliere zonne-energie, Natuur- en bosgebieden, Gebouwde omgeving, Emissies van fijnstof, Groenblauwe infrastructuur
        - Het thema natuurlijk kapitaal bestaat uit de indicatoren **particuliere zonne-energie**, **natuur- en bosgebieden**, **bebouwde omgeving** en **emissies van fijnstof naar de lucht**.  
        - Zoals gedefinieerd door het CBS, is de indicator **particuliere zonne-energie** de geïnstalleerde capaciteit van zonne-energie-installaties in watt per woning aan het einde van het referentiejaar. Dit betreft de capaciteit van zonnepaneleninstallaties bij woningen, gedeeld door het totale aantal woningen, dus zowel woningen met als zonder zonnepanelen.  
        - Zoals gedefinieerd door het CBS, is de indicator **natuur- en bosgebieden** het percentage van het totale landoppervlak dat bestaat uit bos en open natuurlijk terrein.  
        - **Bos**: terrein beplant met bomen, bedoeld voor houtproductie en/of natuurbeheer, inclusief onverharde en halfverharde wegen.  
        - **Natuurlijk terrein**: terrein in droge en natte natuurlijke staat.  
        - Zoals gedefinieerd door het CBS, is de indicator **bebouwde omgeving** het land dat wordt gebruikt voor wonen, werken, winkelen, recreatie, cultuur en openbare voorzieningen als percentage van het totale landoppervlak.  
        - Zoals gedefinieerd door het CBS, is de indicator **emissies van fijnstof naar de lucht** de jaarlijkse gemiddelde fijnstofemissie naar de lucht. De fijnere fractie van fijnstof bestaat uit deeltjes met een diameter van minder dan 2,5 micrometer.  
        - De indicator **particuliere zonne-energie** bevat gegevens voor de jaren 2013 tot en met 2022.  
        - De indicatoren **natuur- en bosgebieden** en **bebouwde omgeving** bevatten gegevens voor de jaren 2015 en 2017.  
        - De indicator **emissies van fijnstof naar de lucht** bevat gegevens voor de jaren 2015 en 2019 tot en met 2022.  
        - Het thema **natuurlijk kapitaal** is geconstrueerd voor het jaar 2015.
    """,
    "Natuur":"""
        **Welkom bij het thema Natuur**
        - In dit thema zijn de volgende indicatoren opgenomen: ....
        - Het subthema natuur bestaat uit de indicatoren ‘natuurgebied per inwoner’, ‘natuur- en bosgebieden’ en ‘afstand tot openbaar groen’.  
        - Zoals gedefinieerd door het CBS, is de indicator natuurgebied per inwoner de hoeveelheid hectares bos en open natuurlijk terrein per 1000 inwoners.  
        - **Bos**: terrein beplant met bomen, bedoeld voor houtproductie en/of natuurbeheer, inclusief onverharde en halfverharde wegen.  
        - **Natuurlijk terrein**: terrein in droge en natte natuurlijke staat.  
        - Zoals gedefinieerd door het CBS, is de indicator natuur- en bosgebieden het percentage van het totale landoppervlak dat bestaat uit bos en open natuurlijk terrein.  
        - **Bos**: terrein beplant met bomen, bedoeld voor houtproductie en/of natuurbeheer, inclusief onverharde en halfverharde wegen.  
        - **Natuurlijk terrein**: terrein in droge en natte natuurlijke staat.  
        - Zoals gedefinieerd door het CBS, is de indicator afstand tot openbaar groen de gemiddelde afstand van alle inwoners in een gebied tot het dichtstbijzijnde openbare groen, berekend over de weg.  
        - **Openbaar groen** is grond die wordt gebruikt als park of openbare tuin, voor dagrecreatie, natuur of als bos. De grond kan zowel privé als openbaar toegankelijk zijn en heeft een minimale grootte van één hectare.  
        - De indicatoren ‘natuurgebied per inwoner’, ‘natuur- en bosgebieden’ en ‘afstand tot openbaar groen’ bevatten gegevens voor de jaren 2015 en 2017. Het subthema natuur is geconstrueerd voor de jaren 2015 en 2017.
    """,
    "Afstand tot woonvoorzieningen":"""
        **Welkom bij het thema Afstand tot Woonvoorzieningen**
        - Het CBS gebruikt de vijf indicatoren **tevredenheid met de woonomgeving**, **tevredenheid met de woning**, **afstand tot sportterrein**, **afstand tot basisschool** en **afstand tot café etc.** voor het thema **Wonen**.  
        - Aangezien de door het CBS verstrekte gegevens voor de indicatoren **tevredenheid met de woonomgeving** en **tevredenheid met de woning** onvolledig zijn, doordat gegevens over verschillende gemeenten ontbreken, zijn deze indicatoren niet opgenomen in de constructie van het thema Wonen. Het thema is daarom hernoemd naar **Afstand tot woonvoorzieningen**, omdat de drie indicatoren met een afstandsmaat hierin wel zijn opgenomen.  
        - Zoals gedefinieerd door het CBS, is de indicator **afstand tot sportterrein** de gemiddelde afstand, berekend over de weg, van alle inwoners in een gebied tot een terrein dat wordt gebruikt voor sportactiviteiten. Dit omvat sportterreinen, sporthallen, zwembaden, kunstijsbanen, motorcrossbanen en bosgebieden binnen een sportterrein, inclusief collectieve parkeerplaatsen en tribunes. Het terrein heeft een minimale grootte van 0,5 hectare.  
        - Zoals gedefinieerd door het CBS, is de indicator **afstand tot basisschool** de gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde basisschool, berekend over de weg. Het basisonderwijs omvat alleen basisscholen zoals geregistreerd bij de Dienst Uitvoering Onderwijs (DUO). Speciaal basisonderwijs en speciale scholen zijn niet inbegrepen.  
        - Zoals gedefinieerd door het CBS, is de indicator **afstand tot café etc.** de gemiddelde afstand van alle inwoners in een gebied tot de dichtstbijzijnde horecagelegenheid, zoals een café, koffiehuis, coffeeshop, discotheek, seks-/nachtclub of partycentrum, berekend over de weg.  
        - Beschikbare gegevens per indicator:  
        - **Afstand tot sportterrein**: 2015 en 2017  
        - **Afstand tot basisschool**: 2013 tot en met 2023  
        - **Afstand tot café etc.**: 2013 tot en met 2023  
        - Het thema **Afstand tot woonvoorzieningen** is geconstrueerd voor de jaren 2015 en 2017.
    """,
    "Samenleving":"""
        **Welkom bij het thema Samenleving**
        - Het thema **samenleving** bestaat uit de indicatoren **contact met familie, vrienden of buren**, **vertrouwen in instituties**, **vertrouwen in anderen**, **vrijwilligerswerk** en **tevredenheid met het sociale leven**.  
        - Zoals gedefinieerd door het CBS, is de indicator **contact met familie, vrienden of buren** het percentage personen van 15 jaar en ouder dat gemiddeld minstens één keer per week contact heeft met familie, vrienden of buren. Dit betreft alle vormen van contact. Het is het gemiddelde van de indicatoren "minstens wekelijks contact met familie", "minstens wekelijks contact met vrienden" en "minstens wekelijks contact met buren".  
        - Zoals gedefinieerd door het CBS, is de indicator **vertrouwen in instituties** het percentage personen van 15 jaar en ouder dat vertrouwen heeft in drie instituties (Tweede Kamer, politie en rechters). De indicator is het gemiddelde van de drie scores.  
        - Zoals gedefinieerd door het CBS, is de indicator **vertrouwen in anderen** het percentage personen van 15 jaar en ouder dat het eens is met de stelling dat de meeste mensen over het algemeen te vertrouwen zijn. Dit wordt ook wel **gegeneraliseerd vertrouwen** genoemd.  
        - Zoals gedefinieerd door het CBS, is de indicator **vrijwilligerswerk** het percentage personen van 15 jaar en ouder dat in de afgelopen 12 maanden vrijwilligerswerk heeft gedaan voor organisaties of verenigingen. Dit kan zowel bestuurlijk werk als andere activiteiten betreffen.  
        - Zoals gedefinieerd door het CBS, is de indicator **tevredenheid met het sociale leven** het percentage personen in Nederland van 18 jaar en ouder dat een score van 7 tot 10 geeft op de vraag:  
        - *"Kunt u op een schaal van 1 tot 10 aangeven in hoeverre u tevreden bent met uw sociale leven? Een 1 staat voor volledig ontevreden en een 10 voor volledig tevreden."*  
        - Een score van 7 tot 10 wordt geclassificeerd als **(zeer) tevreden**.  
        - Voor de vijf indicatoren **contact met familie, vrienden of buren**, **vertrouwen in instituties**, **vertrouwen in anderen**, **vrijwilligerswerk** en **tevredenheid met het sociale leven** zijn gegevens beschikbaar voor de jaren 2013 tot en met 2023.  
        - Het thema **samenleving** is geconstrueerd met deze vijf indicatoren voor de jaren 2013 tot en met 2023.
    """,
}

Sources = {
        "Bevolking met een startkwalificatie": """ 
        - Source for spillover calculation: https://www.sciencedirect.com/science/article/pii/S0166046222000163 
    """,
        "Werkloosheid": """
        - Source for spillover calculation: https://www.sciencedirect.com/science/article/pii/S0166046222000163 
    """,
        "Afstand tot ov": """ 
        - Source for spillover calculation: https://www.researchgate.net/figure/Reported-values-for-willingness-to-walk-to-public-transport-in-meters-and-for-the_tbl1_358628261 
    """,
        "Afstand tot sportterrein": """ 
        - Source for spillover calculation: https://www.sciencedirect.com/science/article/abs/pii/S1353829219304861?via%3Dihub
    """,
        "Afstand tot basisschool": """ 
        - Source for spillover calculation: https://ijbnpa.biomedcentral.com/articles/10.1186/1479-5868-5-1
    """,
        "Afstand tot café e.d.": """
        - Source for spillover calculation: https://www.cdc.gov/pcd/issues/2015/15_0065.htm#:~:text=The%20median%20distance%20to%20sit,0.4%20miles%20to%20grocery%2Fsupermarkets.
    """,
        "Vertrouwen in instituties": """
        - Source for spillover calculation: https://ifh.wiwi.uni-goettingen.de/site/assets/files/8720/ifh_wp-41_2023.pdf
    """,
        "Vertrouwen in anderen": """ 
        - Source for spillover calculation: https://ifh.wiwi.uni-goettingen.de/site/assets/files/8720/ifh_wp-41_2023.pdf
    """,
        "Afstand tot openbaar groen": """ 
        - Source for spillover calculation: https://pdf.sciencedirectassets.com/271856/1-s2.0-S0143622821X00161/1-s2.0-S0143622822000443/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLWVhc3QtMSJGMEQCIDI1cXNOXi26MOMKhMD3oEF6bpPaoYlmGXIpM1rX3WUeAiAf1jWkQ2O2geUxauNJN%2BjNAb%2B74GRSsW%2Bpeet9HWfJwiq8BQio%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAUaDDA1OTAwMzU0Njg2NSIMQAToFxN5KD1yW4B9KpAFTbUl%2FvHHjA3j%2BXOtna5Xmh7nm%2BMRyBKrp%2Fh2yDjju28pCIciWXfwau7eIOYf6NFEjxWNHkGc8UxUn7vtwTydSmw3%2BZHX6Y4TPzdqdplNSxPSjfoRdk9TpLTBiSrlIKzBht2WfSW%2B%2BNZQemyZB3dQoz3hXi0LiXD3n%2Bul%2F%2F%2FUuQ6sgQ6RU40Smq%2BhoEEeLhk39P4cZaHDmtQhOEMhQvpAyCwHc0aXhKDnuvlkg6y9i5IxL2xSr5EhfhdrSW4%2BkOf%2F4pwDVQ65YLdgYm71dYpV2SnalampwUNRJdSbgJCc0vbc8azmkpT39XORXErkM0FU%2BjixgQVT9qFB3kGNw1nXAwr4wQa5OLoRo2ePNYoYOiN29irbmLciXtYHlqsdF1z6O4O8sqnHpMXyYuaOR1t9lcdeTY4ROa8p0ieLPFcx9rzYHVBJ%2Bod%2BtBEWJ9qWpnOzxx%2FfTLaHeVrxMq4o89Xku8h1AfpfWHiLMZZcplHdIf787c1wTCgAJZ5gTeZW8VpnVfo0lIfuHTyw6uZlWDf6DC6ZdrqFNamyyQi2r7%2BOaQY63TI%2FLopiWeCRP%2FLD4sQeds4n96p5RKgjwrCcwm6MRprqgmvgXDqpPIcR%2BMvDGte3qu2yF9VoBEl7MxGktSJr5vxD8ZLngC8OZPpywRm9EhMi6e63lE202KSs25IhbQaQaHqSoT%2F0%2BgZjgFbJ%2Bv3FKngf7FWI90jO6hYtP0q0s%2FCDyfRV%2FjXA0matp3A5Yc5ClfZsIKxI0crGkEPi9Hecij7mMXt%2BxRiFFskKNp8aAf7W9BNbD89FMR6TULOVr3Hm8pF4HmA1Cd0slUwiR3aXMHI%2FmBL%2F0fU8wRX2TiRoIIYrWYiCndTQKmmLUj7gjR4wyZr9uQY6sgH39aiIjyCQjViIGxqXwzaHRLOLbj3KPcer91muLfXbq%2FfwQyPN%2B3aHO417%2FExOAX8OsgLrlf%2FDsvIAdOIMyAPinRuMQmetm95L0kSHcj5mmxnpds%2BLXIryHQzqHMz8G8PLmcKyTG9HosYiEIoGSp5cIqGIdSW6%2F3vFikLCqfV%2FehKLK4AtvFYBcEmF1JeVXZV3TOjIpnxsek77NsEF0ko43Q%2BUuKDCVnzW6n%2Fv0VBJN%2BQV&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20241121T154228Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYYS3KVGZV%2F20241121%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=2d71f50f79ae470cfd6b4a04e1bcd56d86fac47e70e4ac3fa7471f41be7af09e&hash=3f1a4f087252bb734def0d4bc943b7ac490d50c3ee07949d17c39d016de29a5c&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S0143622822000443&tid=spdf-91fa4363-540b-499e-8423-05a32d28bef6&sid=ceb2aa3282359042885b7ee454d5e02afb8dgxrqb&type=client&tsoh=d3d3LnNjaWVuY2VkaXJlY3QuY29t&ua=080c5e0150530c045052&rr=8e61ca317ed29f5d&cc=nl
    """,
        "Natuur- en bosgebieden": """ 
        - Source for spillover calculation: https://ijbnpa.biomedcentral.com/articles/10.1186/1479-5868-5-1
    """,
        "Particuliere zonne-energie": """
        - Source for spillover calculation: https://www.cdc.gov/pcd/issues/2015/15_0065.htm#:~:text=The%20median%20distance%20to%20sit,0.4%20miles%20to%20grocery%2Fsupermarkets.
    """,
        "Emissies van fijnstof naar lucht": """ 
        - Source for spillover calculation: https://www.rivm.nl/ggd-richtlijn-medische-milieukunde-luchtkwaliteit-en-gezondheid/gezondheidseffecten-luchtverontreiniging/luchtkwaliteit-invloed-drukke-wegen
    """,
}
