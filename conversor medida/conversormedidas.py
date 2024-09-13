import pandas as pd


def cm_a_pulgadas(cm):
    return cm / 2.54


# Leer el archivo excel, podria ser también el csv
df = pd.read_excel("muebles_medidas.xlsx")

# Añadir una columna al Dataframe que sea de pulgadas y se rellene con el calculo cm / 2.54
df["Pulgadas"] = df["Centímetros"].apply(cm_a_pulgadas)

df.to_excel("muebles_medidas_convertidas.xlsx", index=False)
print(
    "Conversión completada y guardada en un nuevo archivo llamado 'muebles_medidas_convertidas.xlsx'"
)
