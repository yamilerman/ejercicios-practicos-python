import pandas as pd

# Dataframe es la info básica con el cnombre de las piezas y centrimetros para poder armar un Excel

data = {
    "Piezas": ["Pata", "Armazon", "Puerta", "Estante", "Tiradores"],
    "Centímetros": [120, 30, 50, 140, 90],
}

df = pd.DataFrame(data)

# Guardar el dataframe en un archivo excel

df.to_csv("muebles_medidas.csv", index=False)
