import pandas as pd
import re
import numpy as np

# Importamos el archivo csv generado previamente que contiene los comentarios de YouTube
df = pd.read_csv('youtube_comments.csv')

# Convertimos todos los datos de "Comment" a tipo string
df['Comment'] = df['Comment'].astype(str)

# Aplicamos expresiones regulares para eliminar caracteres indeseados, enlaces y luego convertimos todo a minúsculas 
df['Comment'] = df['Comment'].apply(lambda x: re.sub(r'[^\w\s]', '', x))
df['Comment'] = df['Comment'].apply(lambda x: re.sub(r'\s+', ' ', x))
df['Comment'] = df['Comment'].apply(lambda x: re.sub(r'http\S+|www.\S+', '', x))
df['Comment'] = df['Comment'].apply(lambda x: re.sub(r'\d+', '', x))
df['Comment'] = df['Comment'].apply(lambda x: x.lower().strip())

# Reemplazamos los comentarios en blanco con "NaN"
df['Comment'].replace('', np.nan, inplace=True)

# Eliminamos todas las filas que tengan valor "NaN" en la celda de la columna "Comment"
df.dropna(subset=['Comment'], inplace=True)

# Eliminamos todos los comentarios duplicados y solo nos quedamos con uno de ellos
df.drop_duplicates(subset='Comment', keep='first', inplace=True)

# Si existe la columna 'ID', la eliminamos
if 'ID' in df.columns:
    df = df.drop(columns=['ID'])

# Agregamos la nueva columna 'ID' al principio del DataFrame
df = df.reset_index(drop=True)
df.insert(0, 'ID', df.index + 1)

# Guardamos el resultado de la limpieza sin un índice
df.to_csv('cleaned_youtube_comments.csv', index=False)