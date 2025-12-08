import pandas as pd

# --- DATOS DE LOS EQUIPOS EXPANDIDOS ---

equipos_data = {
    "Inglaterra": {
        "Premier League": [
            "Arsenal", "Aston Villa", "Bournemouth", "Brentford", "Brighton", "Chelsea", 
            "Crystal Palace", "Everton", "Fulham", "Ipswich Town", "Leicester City", 
            "Liverpool", "Manchester City", "Manchester United", "Newcastle United", 
            "Nottingham Forest", "Southampton", "Tottenham Hotspur", "West Ham United", "Wolverhampton"
        ],
        "Championship": [
            "Blackburn Rovers", "Bristol City", "Burnley", "Cardiff City", "Coventry City", 
            "Derby County", "Hull City", "Leeds United", "Luton Town", "Middlesbrough", 
            "Millwall", "Norwich City", "Oxford United", "Plymouth Argyle", "Portsmouth", 
            "Preston North End", "QPR", "Sheffield United", "Sheffield Wednesday", 
            "Stoke City", "Sunderland", "Swansea City", "Watford", "West Bromwich Albion"
        ],
        "League One": [
            "Barnsley", "Birmingham City", "Blackpool", "Bolton Wanderers", "Bristol Rovers",
            "Burton Albion", "Cambridge United", "Charlton Athletic", "Crawley Town",
            "Exeter City", "Fleetwood Town", "Huddersfield Town", "Leyton Orient",
            "Lincoln City", "Mansfield Town", "Northampton Town", "Peterborough United",
            "Reading", "Rotherham United", "Shrewsbury Town", "Stevenage", "Stockport County",
            "Wigan Athletic", "Wrexham", "Wycombe Wanderers"
        ]
    },
    "España": {
        "La Liga": [
            "Alavés", "Athletic Club", "Atlético de Madrid", "Barcelona", "Celta de Vigo", 
            "Espanyol", "Getafe", "Girona", "Las Palmas", "Leganés", "Mallorca", "Osasuna", 
            "Rayo Vallecano", "Real Betis", "Real Madrid", "Real Sociedad", "Real Valladolid", 
            "Sevilla", "Valencia", "Villarreal"
        ],
        "Segunda División": [
            "Albacete", "Almería", "Burgos", "Cádiz", "Cartagena", "Castellón", "Córdoba", 
            "Deportivo La Coruña", "Eibar", "Elche", "Eldense", "Ferrol", "Granada", 
            "Huesca", "Levante", "Málaga", "Mirandés", "Oviedo", "Racing de Santander", 
            "Sporting Gijón", "Tenerife", "Zaragoza"
        ],
        "Primera Federación": [
            "Alcoyano", "Andorra", "Antequera", "Atlético Baleares", "Badajoz",
            "Celta B", "Cultural Leonesa", "Deportivo Fabril", "Extremadura",
            "Fuenlabrada", "Gimnàstic", "Intercity", "Linares", "Murcia",
            "Pontevedra", "Rayo Majadahonda", "Real Madrid Castilla", "San Fernando",
            "Tarazona", "Teruel", "Unionistas", "Villarreal B"
        ]
    },
    "Italia": {
        "Serie A": [
            "Atalanta", "Bologna", "Cagliari", "Como", "Empoli", "Fiorentina", "Genoa", 
            "Inter Milan", "Juventus", "Lazio", "Lecce", "AC Milan", "Monza", "Napoli", 
            "Parma", "Roma", "Torino", "Udinese", "Venezia", "Verona"
        ],
        "Serie B": [
            "Bari", "Brescia", "Carrarese", "Catanzaro", "Cesena", "Cittadella", "Cosenza", 
            "Cremonese", "Frosinone", "Juve Stabia", "Mantova", "Modena", "Palermo", 
            "Pisa", "Reggiana", "Salernitana", "Sampdoria", "Sassuolo", "Spezia", "Südtirol"
        ],
        "Serie C": [
            "Ancona", "Arezzo", "Avellino", "Benevento", "Carpi", "Catania",
            "Cesena", "Fermana", "Fiorenzuola", "Gubbio", "Juve Next Gen",
            "Latina", "LR Vicenza", "Maceratese", "Padova", "Pescara",
            "Piacenza", "Pineto", "Potenza", "Recanatese", "Rimini",
            "Sangiuliano City", "Taranto", "Torres", "Triestina", "Virtus Entella"
        ]
    },
    "Alemania": {
        "Bundesliga": [
            "Augsburg", "Bayer Leverkusen", "Bayern Munich", "Bochum", "Borussia Dortmund", 
            "Borussia M'gladbach", "Eintracht Frankfurt", "Freiburg", "Heidenheim", 
            "Hoffenheim", "Holstein Kiel", "Mainz 05", "RB Leipzig", "St. Pauli", 
            "Stuttgart", "Union Berlin", "Werder Bremen", "Wolfsburg"
        ],
        "2. Bundesliga": [
            "Darmstadt 98", "Elversberg", "Fortuna Düsseldorf", "Greuther Fürth", "Hamburg", 
            "Hannover 96", "Hertha BSC", "Jahn Regensburg", "Kaiserslautern", "Karlsruher", 
            "Köln", "Magdeburg", "Münster", "Nürnberg", "Paderborn", "Schalke 04", "Ulm"
        ],
        "3. Liga": [
            "Aalen", "Arminia Bielefeld", "Bayern Munich II", "Borussia Dortmund II",
            "Braunschweig", "Duisburg", "Dynamo Dresden", "Erzgebirge Aue",
            "Essen", "Freiburg II", "Hallescher", "Ingolstadt", "Kaiserslautern",
            "Meppen", "Offenbach", "Osnabrück", "Saarbrücken", "Sandhausen",
            "Unterhaching", "Verl", "VfB Lübeck", "Viktoria Köln", "Waldhof Mannheim",
            "Wehen Wiesbaden", "Würzburger Kickers", "Zwickau"
        ]
    },
    "Francia": {
        "Ligue 1": [
            "Angers", "Auxerre", "Brest", "Le Havre", "Lens", "Lille", "Lyon", "Marseille", 
            "Monaco", "Montpellier", "Nantes", "Nice", "PSG", "Reims", "Rennes", 
            "Saint-Étienne", "Strasbourg", "Toulouse"
        ],
        "Ligue 2": [
            "Ajaccio", "Amiens", "Annecy", "Bastia", "Caen", "Clermont Foot", "Dunkerque", 
            "Grenoble", "Guingamp", "Laval", "Lorient", "Martigues", "Metz", "Paris FC", 
            "Pau", "Red Star", "Rodez", "Troyes", "Valenciennes"
        ],
        "National": [
            "Avranches", "Bourg-en-Bresse", "Châteauroux", "Cholet", "Concarneau",
            "Dijon", "Épinal", "GOAL FC", "Le Mans", "Marignane Gignac",
            "Nancy", "Niort", "Orléans", "Red Star", "Rouen", "Sedan",
            "Sochaux", "Versailles", "Villefranche"
        ]
    },
    "Portugal": {
        "Primeira Liga": [
            "Arouca", "AVS", "Benfica", "Boavista", "Braga", "Casa Pia", "Estoril", 
            "Estrela Amadora", "Famalicão", "Farense", "Gil Vicente", "Moreirense", 
            "Nacional", "Porto", "Rio Ave", "Santa Clara", "Sporting CP", "Vitória Guimarães"
        ],
        "Segunda Liga": [
            "Académico Viseu", "B SAD", "Belenses", "Benfica B", "Braga B",
            "Covilhã", "Feirense", "Leixões", "Mafra", "Marítimo",
            "Oliveirense", "Penafiel", "Porto B", "Sporting CP B", "Torreense",
            "Trofense", "União Madeira", "Varzim", "Vilafranquense"
        ]
    },
    "Países Bajos": {
        "Eredivisie": [
            "Ajax", "Almere City", "AZ Alkmaar", "Feyenoord", "Fortuna Sittard", 
            "Go Ahead Eagles", "Groningen", "Heerenveen", "Heracles", "NAC Breda", 
            "NEC Nijmegen", "PEC Zwolle", "PSV Eindhoven", "RKC Waalwijk", "Sparta Rotterdam", 
            "Twente", "Utrecht", "Willem II"
        ],
        "Eerste Divisie": [
            "ADO Den Haag", "Cambuur", "Den Bosch", "Dordrecht", "Eindhoven",
            "Emmen", "Excelsior", "Graafschap", "Helmond Sport", "Jong Ajax",
            "Jong AZ", "Jong PSV", "Jong Utrecht", "Maastricht", "MVV",
            "NAC Breda", "Oss", "Roda JC", "Telstar", "TOP Oss",
            "Volendam", "VVV-Venlo"
        ]
    },
    "Bélgica": {
        "Primera División": [
            "Anderlecht", "Antwerp", "Cercle Brugge", "Charleroi", "Club Brugge",
            "Eupen", "Genk", "Gent", "Kortrijk", "Mechelen",
            "OH Leuven", "RWD Molenbeek", "Seraing", "Standard Liège", "Union SG",
            "Westerlo", "Zulte Waregem"
        ],
        "Segunda División": [
            "Beerschot", "Beveren", "Dender", "Deinze", "Francs Borains",
            "Heist", "KVC Westerlo", "Lierse Kempenzonen", "Lommel",
            "Oostende", "Patro Eisden", "RFC Liège", "RSCA Futures",
            "SL16 FC", "Sint-Truiden", "Virton"
        ]
    },
    "Escocia": {
        "Premiership": [
            "Aberdeen", "Celtic", "Dundee United", "Hearts", "Hibernian",
            "Kilmarnock", "Motherwell", "Rangers", "Ross County", "St. Johnstone",
            "St. Mirren"
        ],
        "Championship": [
            "Airdrieonians", "Arbroath", "Ayr United", "Dunfermline Athletic",
            "Greenock Morton", "Inverness CT", "Partick Thistle", "Queen's Park",
            "Raith Rovers"
        ]
    },
    "Turquía": {
        "Süper Lig": [
            "Adana Demirspor", "Alanyaspor", "Antalyaspor", "Beşiktaş", "Bodrum", "Eyüpspor", 
            "Fenerbahçe", "Galatasaray", "Gaziantep", "Göztepe", "Hatayspor", "Başakşehir", 
            "Kasımpaşa", "Kayserispor", "Konyaspor", "Rizespor", "Samsunspor", "Sivasspor", "Trabzonspor"
        ],
        "TFF 1. Lig": [
            "Altay", "Ankara Keçiörengücü", "Bandırmaspor", "Boluspor", "Çaykur Rizespor",
            "Erzurumspor", "Eskişehirspor", "Giresunspor", "Göztepe", "Kocaelispor",
            "Manisa FK", "Pendikspor", "Sakaryaspor", "Samsunspor", "Şanlıurfaspor",
            "Tuzlaspor", "Ümraniyespor", "Yeni Malatyaspor"
        ]
    },
    "Rusia": {
        "Premier Liga": [
            "Akron Tolyatti", "CSKA Moscow", "Dynamo Moscow", "Krasnodar",
            "Lokomotiv Moscow", "Rubin Kazan", "Spartak Moscow", "Zenit St. Petersburg",
            "Akhmat Grozny", "Baltika Kaliningrad", "Fakel Voronezh", "Khimki",
            "Krylia Sovetov", "Nizhny Novgorod", "Orenburg", "Rostov", "Sochi", "Ural"
        ],
        "First League": [
            "Alania Vladikavkaz", "Arsenal Tula", "Avangard Kursk", "Chaika Peschanokopskoye",
            "Enisey Krasnoyarsk", "KAMAZ", "Kuban Krasnodar", "Leningradets",
            "Mashuk-KMV", "Neftekhimik", "Rodina Moscow", "Shinnik Yaroslavl",
            "SKA-Khabarovsk", "Torpedo Moscow", "Tyumen", "Veles Moscow", "Volgar Astrakhan"
        ]
    },
    "Brasil": {
        "Brasileirão": [
            "Athletico Paranaense", "Atlético Goianiense", "Atlético Mineiro", "Bahia", 
            "Botafogo", "Corinthians", "Criciúma", "Cruzeiro", "Cuiabá", "Flamengo", 
            "Fluminense", "Fortaleza", "Grêmio", "Internacional", "Juventude", "Palmeiras", 
            "Red Bull Bragantino", "São Paulo", "Vasco da Gama", "Vitória"
        ],
        "Série B": [
            "ABC", "América Mineiro", "Avaí", "Brussels", "Ceará", "Chapecoense",
            "CRB", "Goiás", "Guarani", "Ituano", "Mirassol", "Novorizontino",
            "Operário", "Paysandu", "Ponte Preta", "Santos", "Sport Recife",
            "Tombense", "Vila Nova"
        ]
    },
    "Argentina": {
        "Liga Profesional": [
            "Argentinos Juniors", "Atlético Tucumán", "Banfield", "Barracas Central", 
            "Belgrano", "Boca Juniors", "Central Córdoba", "Defensa y Justicia", 
            "Estudiantes", "Gimnasia", "Godoy Cruz", "Huracán", "Independiente", 
            "Independiente Rivadavia", "Instituto", "Lanús", "Newell's", "Platense", 
            "Racing Club", "Riestra", "River Plate", "Rosario Central", "San Lorenzo", 
            "Sarmiento", "Talleres", "Tigre", "Unión", "Vélez Sarsfield"
        ],
        "Primera Nacional": [
            "Agropecuario", "Almagro", "Almirante Brown", "All Boys", "Atlanta",
            "Atlético Rafaela", "Brown de Adrogué", "Chacarita Juniors", "Chaco For Ever",
            "Colón", "Deportivo Madryn", "Deportivo Maipú", "Deportivo Morón",
            "Estudiantes RC", "Ferro Carril Oeste", "Gimnasia Jujuy", "Gimnasia Mendoza",
            "Güemes", "Mitre", "Nueva Chicago", "Patronato", "Quilmes", "San Martín SJ",
            "San Martín Tucumán", "San Telmo", "Temperley", "Trinidad", "Villa Dálmine"
        ]
    },
    "México": {
        "Liga MX": [
            "América", "Atlas", "Atlético San Luis", "Cruz Azul", "Guadalajara",
            "Juárez", "León", "Mazatlán", "Monterrey", "Necaxa",
            "Pachuca", "Puebla", "Querétaro", "Santos Laguna", "Tigres UANL",
            "Tijuana", "Toluca", "UNAM Pumas"
        ],
        "Liga de Expansión": [
            "Alebrijes Oaxaca", "Atlante", "Cancún", "Celaya", "Dorados",
            "Durango", "Mineros", "Morelia", "Raya2", "Tampico Madero",
            "Tepatitlán", "UAT", "UdeG", "Venados", "Zacatecas"
        ]
    },
    "Estados Unidos": {
        "MLS": [
            "Atlanta United", "Austin FC", "Charlotte FC", "Chicago Fire", "Colorado Rapids",
            "Columbus Crew", "D.C. United", "FC Cincinnati", "FC Dallas", "Houston Dynamo",
            "Inter Miami", "LA Galaxy", "LAFC", "Minnesota United", "Nashville SC",
            "New England Revolution", "New York City FC", "New York Red Bulls", "Orlando City",
            "Philadelphia Union", "Portland Timbers", "Real Salt Lake", "San Jose Earthquakes",
            "Seattle Sounders", "Sporting Kansas City", "St. Louis City", "Toronto FC", "Vancouver Whitecaps"
        ],
        "USL Championship": [
            "Birmingham Legion", "Charleston Battery", "Colorado Springs Switchbacks",
            "Detroit City", "El Paso Locomotive", "Hartford Athletic", "Indy Eleven",
            "Las Vegas Lights", "Loudoun United", "Louisville City", "Memphis 901",
            "Miami FC", "Monterey Bay", "New Mexico United", "North Carolina FC",
            "Oakland Roots", "Orange County SC", "Phoenix Rising", "Pittsburgh Riverhounds",
            "Rhode Island FC", "Sacramento Republic", "San Antonio FC", "Tampa Bay Rowdies",
            "Tulsa Roughnecks"
        ]
    },
    "Japón": {
        "J1 League": [
            "Albirex Niigata", "Cerezo Osaka", "FC Tokyo", "Gamba Osaka", "Hokkaido Consadole Sapporo",
            "Júbilo Iwata", "Kashiwa Reysol", "Kawasaki Frontale", "Kashiwa Antlers",
            "Nagoya Grampus", "Sanfrecce Hiroshima", "Shonan Bellmare", "Sagan Tosu",
            "Tokyo Verdy", "Urawa Red Diamonds", "Vissel Kobe", "Yokohama F. Marinos",
            "Yokohama FC"
        ],
        "J2 League": [
            "Blaublitz Akita", "Ehime FC", "Fagiano Okayama", "Fujieda MYFC", "JEF United",
            "Kagoshima United", "Kamatamare Sanuki", "Mito HollyHock", "Montedio Yamagata",
            "Oita Trinita", "Omiya Ardija", "Renofa Yamaguchi", "Roasso Kumamoto",
            "Shimizu S-Pulse", "Thespakusatsu Gunma", "Tochigi SC", "Tokushima Vortis",
            "V-Varen Nagasaki", "Ventforet Kofu", "Zweigen Kanazawa"
        ]
    },
    "Corea del Sur": {
        "K League 1": [
            "Daegu FC", "Daejeon Hana Citizen", "Gangwon FC", "Gimcheon Sangmu",
            "Gwangju FC", "Incheon United", "Jeju United", "Jeonbuk Hyundai Motors",
            "Pohang Steelers", "Seoul", "Suwon FC", "Ulsan Hyundai"
        ],
        "K League 2": [
            "Ansan Greeners", "Busan IPark", "Bucheon FC 1995", "Cheonan City",
            "Cheongju FC", "Chungbuk Cheongju", "FC Anyang", "Gimpo FC",
            "Gyeongnam FC", "Jeonnam Dragons", "Seongnam FC", "Suwon Samsung Bluewings"
        ]
    },
    "Arabia Saudita": {
        "Saudi Pro League": [
            "Al-Ahli", "Al-Ettifaq", "Al-Fateh", "Al-Fayha", "Al-Hazem",
            "Al-Hilal", "Al-Ittihad", "Al-Khaleej", "Al-Nassr", "Al-Okhdood",
            "Al-Qadsiah", "Al-Raed", "Al-Riyadh", "Al-Shabab", "Al-Taawoun",
            "Al-Tai", "Al-Wehda", "Damac"
        ]
    },
    "Suiza": {
        "Super League": [
            "Basel", "Grasshopper", "Lausanne", "Lugano", "Luzern",
            "Servette", "St. Gallen", "Winterthur", "Young Boys", "Zürich"
        ]
    },
    "Austria": {
        "Bundesliga": [
            "Austria Klagenfurt", "Austria Lustenau", "Austria Wien", "LASK",
            "Rapid Wien", "Red Bull Salzburg", "Sturm Graz", "TSV Hartberg",
            "Wolfsberger AC", "WSG Tirol"
        ]
    },
    "Dinamarca": {
        "Superliga": [
            "AGF", "Brøndby", "Copenhagen", "FC Nordsjælland", "Hvidovre",
            "Kolding IF", "Lyngby", "Midtjylland", "Randers", "Silkeborg",
            "Vejle", "Viborg"
        ]
    },
    "Noruega": {
        "Eliteserien": [
            "Bodø/Glimt", "Brann", "Fredrikstad", "HamKam", "KFUM Oslo",
            "Kristiansund", "Lillestrøm", "Molde", "Odd", "Rosenborg",
            "Sandefjord", "Sarpsborg 08", "Stabæk", "Strømsgodset", "Tromsø", "Vålerenga"
        ]
    },
    "Suecia": {
        "Allsvenskan": [
            "AIK", "BK Häcken", "Djurgården", "Elfsborg", "GAIS",
            "Halmstad", "Hammarby", "IFK Göteborg", "IFK Norrköping",
            "Kalmar FF", "Malmö FF", "Mjällby", "Sirius", "Värnamo",
            "Västerås SK", "Örebro"
        ]
    }
}

# --- PROCESAMIENTO ---

lista_filas = []

for pais, ligas in equipos_data.items():
    for liga, equipos in ligas.items():
        for equipo in equipos:
            lista_filas.append([pais, liga, equipo, ""]) # Elegible vacío

# Crear DataFrame
df = pd.DataFrame(lista_filas, columns=["Pais", "Liga", "Equipo", "Elegible"])

# --- GUARDAR EXCEL ---
nombre_salida = "equipos_completo.xlsx"
df.to_excel(nombre_salida, index=False)

print(f"✅ ¡Listo! Base de datos actualizada.")
print(f"📄 Archivo generado: '{nombre_salida}'")
print(f"🌍 Total de países: {len(equipos_data)}")
print(f"🏆 Total de ligas: {sum(len(ligas) for ligas in equipos_data.values())}")
print(f"⚽ Total de equipos: {len(lista_filas)}")