import pandas as pd

# Création de la liste des correspondances
city_state_mapping = [
    {"City": "Austin", "State": "Texas"},
    {"City": "Oklahoma City", "State": "Oklahoma"},
    {"City": "Memphis", "State": "Tennessee"},
    {"City": "Fort Worth", "State": "Texas"},
    {"City": "Detroit", "State": "Michigan"},
    {"City": "Jacksonville", "State": "Florida"},
    {"City": "Tucson", "State": "Arizona"},
    {"City": "Colorado Springs", "State": "Colorado"},
    {"City": "San Jose", "State": "California"},
    {"City": "Los Angeles", "State": "California"},
    {"City": "Philadelphia", "State": "Pennsylvania"},
    {"City": "Houston", "State": "Texas"},
    {"City": "San Antonio", "State": "Texas"},
    {"City": "San Diego", "State": "California"},
    {"City": "Mesa", "State": "Arizona"},
    {"City": "Columbus", "State": "Ohio"},
    {"City": "Phoenix", "State": "Arizona"},
    {"City": "Kansas City", "State": "Missouri"},
    {"City": "Omaha", "State": "Nebraska"},
    {"City": "Charlotte", "State": "North Carolina"},
    {"City": "New York", "State": "New York"},
    {"City": "Raleigh", "State": "North Carolina"},
    {"City": "El Paso", "State": "Texas"},
    {"City": "Miami", "State": "Florida"},
    {"City": "Washington", "State": "District of Columbia"},
    {"City": "San Francisco", "State": "California"},
    {"City": "Boston", "State": "Massachusetts"},
    {"City": "Indianapolis", "State": "Indiana"},
    {"City": "Las Vegas", "State": "Nevada"},
    {"City": "Chicago", "State": "Illinois"},
    {"City": "Atlanta", "State": "Georgia"},
    {"City": "Denver", "State": "Colorado"},
    {"City": "Milwaukee", "State": "Wisconsin"},
    {"City": "Virginia Beach", "State": "Virginia"},
    {"City": "Baltimore", "State": "Maryland"},
    {"City": "Nashville", "State": "Tennessee"},
    {"City": "Seattle", "State": "Washington"},
    {"City": "Portland", "State": "Oregon"},
    {"City": "Louisville", "State": "Kentucky"},
    {"City": "Fresno", "State": "California"},
    {"City": "Sacramento", "State": "California"},
    {"City": "Dallas", "State": "Texas"},
    {"City": "Albuquerque", "State": "New Mexico"}
]

# Convertir en DataFrame
df_city_state = pd.DataFrame(city_state_mapping)

# Sauvegarder le fichier
df_city_state.to_excel("city_state_mapping.xlsx", index=False)
