import pandas as pd

# --- DATOS DE LOS EQUIPOS (Temporada 2025/2026 Estiimada) ---

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
            "Pau", "Red Star", "Rodez", "Troyes"
        ]
    },
    "Portugal": {
        "Primeira Liga": [
            "Arouca", "AVS", "Benfica", "Boavista", "Braga", "Casa Pia", "Estoril", 
            "Estrela Amadora", "Famalicão", "Farense", "Gil Vicente", "Moreirense", 
            "Nacional", "Porto", "Rio Ave", "Santa Clara", "Sporting CP", "Vitória Guimarães"
        ]
    },
    "Países Bajos": {
        "Eredivisie": [
            "Ajax", "Almere City", "AZ Alkmaar", "Feyenoord", "Fortuna Sittard", 
            "Go Ahead Eagles", "Groningen", "Heerenveen", "Heracles", "NAC Breda", 
            "NEC Nijmegen", "PEC Zwolle", "PSV Eindhoven", "RKC Waalwijk", "Sparta Rotterdam", 
            "Twente", "Utrecht", "Willem II"
        ]
    },
    "Turquía": {
        "Süper Lig": [
            "Adana Demirspor", "Alanyaspor", "Antalyaspor", "Beşiktaş", "Bodrum", "Eyüpspor", 
            "Fenerbahçe", "Galatasaray", "Gaziantep", "Göztepe", "Hatayspor", "Başakşehir", 
            "Kasımpaşa", "Kayserispor", "Konyaspor", "Rizespor", "Samsunspor", "Sivasspor", "Trabzonspor"
        ]
    },
    "Brasil": {
        "Brasileirão": [
            "Athletico Paranaense", "Atlético Goianiense", "Atlético Mineiro", "Bahia", 
            "Botafogo", "Corinthians", "Criciúma", "Cruzeiro", "Cuiabá", "Flamengo", 
            "Fluminense", "Fortaleza", "Grêmio", "Internacional", "Juventude", "Palmeiras", 
            "Red Bull Bragantino", "São Paulo", "Vasco da Gama", "Vitória"
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
print(f"⚽ Total de equipos: {len(lista_filas)}")