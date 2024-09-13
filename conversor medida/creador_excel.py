import pandas as pd

# Dataframe

data = {
    "Piezas": ["Pata", "Armazon", "Puerta", "Estante", "Tiradores"],
    "Centímetros": [120, 30, 50, 140, 90],
}

df = pd.DataFrame(data)

# Guardar el dataframe en un archivo excel

df.to_excel("muebles_medidas.xlsx", index=False)
