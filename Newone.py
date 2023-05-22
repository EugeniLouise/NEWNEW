

import pandas as pd

# Ruta y nombre de los archivos XLSX
archivo1 = 'C:/Users/Eugenia Subirons/OneDrive - GRUPOTREBOL/Pruebas_PYCHARM/C4_medperup_11.csv'
archivo2 = 'C:/Users/Eugenia Subirons/OneDrive - GRUPOTREBOL/Pruebas_PYCHARM/C4_medperup_22.csv'


# Leer los archivos CSV utilizando pandas
df1 = pd.read_csv(archivo1)
df2 = pd.read_csv(archivo2)


# Concatenar los DataFrames uno debajo del otro
df_combined = pd.concat([df1, df2], ignore_index=True)

# Guardar el DataFrame combinado en un nuevo archivo CSV
df_combined.to_csv('C:/Users/Eugenia Subirons/OneDrive - GRUPOTREBOL/Pruebas_PYCHARM/MEDPERUP_COMBINADO.csv', index=False)

print("Los archivos se han combinado correctamente después de recortar las filas.")

