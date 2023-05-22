

import pandas as pd

# Ruta y nombre de los archivos Excel
archivo1 = 'C:/Users/Eugenia Subirons/Downloads/Pruebas/C4_medperup_20220101_20220131_18X000000000GDUG.csv'
archivo2 = 'C:/Users/Eugenia Subirons/Downloads/Pruebas/C4_medperup_20220201_20220228_18X000000000GDUG.csv'

# Leer los archivos CSV
df1 = pd.read_csv(archivo1)
df2 = pd.read_csv(archivo2)

# Concatenar los DataFrames uno debajo del otro
df_combined = pd.concat([df1, df2], ignore_index=True)

# Guardar el DataFrame combinado en un nuevo archivo CSV
df_combined.to_csv('C:/Users/Eugenia Subirons/Downloads/Pruebas/MEDPERUP_COMBINADO.csv', index=False)

print("Los archivos se han combinado correctamente.")