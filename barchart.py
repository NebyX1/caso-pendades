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

# Va recorrer la columna "Emoción Dominante" de nuestro dataframe y sumará la cantidad de veces que se repite cada valor
emotion_counts = df['Emoción Dominante'].value_counts()

# Calculamos los porcentajes
total = len(df)
percentages = (emotion_counts / total) * 100

# Paleta de colores no convencionales
colors = ['#66b2ff', '#ff9999', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6', '#ff6666', '#c2f0c2']

# Le indicamos a matplotlib las características con las que debe crear nuestro bar chart
plt.figure(figsize=(10, 5))
bars = percentages.plot(kind='bar', color=colors[:len(emotion_counts)])
plt.title('Gráfico de emociones dominantes')
plt.xlabel('Emoción detectada')
plt.ylabel('Porcentaje')
plt.ylim(0, 100)  # Establecer el límite superior del eje y a 100%

# Añadir los porcentajes arriba de cada barra
for bar in bars.patches:
    yval = bar.get_height()
    bars.text(bar.get_x() + bar.get_width() / 2, yval + 0.5, f'{round(yval, 2)}%', ha='center', va='bottom', fontsize=9)

# Guardamos en la carpeta raíz del proyecto el bar chart generado en formato png
plt.tight_layout()  # Esto asegura que todo quede bien ajustado en la imagen
plt.savefig("barchart.png")

# Esto sirve para mostrar en pantalla el bar chart generado
# plt.show()