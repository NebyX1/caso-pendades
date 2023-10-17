# Importamos las dependencias
import pandas as pd
import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Importamos los módulos de NLTK para quitar palabras de enlace
nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('spanish'))

# Intentamos leer desde el archivo cleaned_youtube_comments.csv
try:
    df = pd.read_csv('cleaned_youtube_comments.csv')
except Exception as e:
    print('Ocurrió un error al intentar leer el archivo:')
    print(str(e))
    exit()

# Guardamos dentro de un dataframe el contenido de la columna "Comment"
df['Comment'] = df['Comment'].fillna('')

# Combinamos todos los comentarios a lo largo de la columna "Comment"
combined_comments = " ".join(df['Comment'])

# Convertimos a tokens las palabras para su mejor tratamiento
word_tokens = nltk.word_tokenize(combined_comments)
filtered_text = " ".join(word for word in word_tokens if word.casefold() not in stop_words)

# Le indicamos el tamaño que queremos que tenga el wordcloud generado y la cantidad de palabras que queremos que aparezcan
wordcloud = WordCloud(width=800, height=400, max_words=120).generate(filtered_text)

# Le indicamos a matplotlib las características con las que debe crear nuestro wordcloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')

# Guardamos en la carpeta raíz del proyecto el wordcloud generado en formato png
wordcloud.to_file("wordcloud.png")

# Esto sirve para mostrar en pantalla el wordcloud generado, por defecto está deshabilitado
# plt.show()