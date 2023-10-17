# Importamos las dependencias
import pandas as pd
import matplotlib.pyplot as plt

# Cargamos el dataframe directamente desde el archivo CSV
try:
    df = pd.read_csv("Analyzed_Comments.csv")
except Exception as e:
    print('Ocurrió un error al intentar cargar el archivo CSV:')
    print(str(e))
    exit()  # Detiene la ejecución del programa

# Va recorrer la columna "Sentimiento" de nuestro dataframe y sumará la cantidad de veces que se repite cada valor disponible (negative, positive y neutral)
sentiment_counts = df['Sentimiento'].value_counts()

# Paleta de colores no convencionales
colors = ['#66b2ff', '#ff9999', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666', '#c2f0c2']

# Le indicamos a matplotlib las características con las que debe crear nuestro piechart
plt.figure(figsize=(10, 5))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=colors[:len(sentiment_counts)])
plt.title('Sentiment Analysis Pie Chart')

# Guardamos en la carpeta raíz del proyecto el piechart generado en formato png
plt.savefig("piechart.png")

# Esto sirve para mostrar en pantalla el piechart generado, por defecto está deshabilitado
# plt.show()
