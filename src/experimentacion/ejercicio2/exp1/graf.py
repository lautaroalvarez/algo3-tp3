import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

columna = 'Cantidad de gimnasios'

titulo = str(columna)+" vs Tiempos de ejecucion (ms)"
labels = ['0001','0011','0111','1111']

df = pd.read_csv("corrida.csv")

agrupado = df.groupby([columna, 'Codigo de vecindad'], as_index=False).mean()

agrupado[[columna, 'Codigo de vecindad', 'Tiempo']].groupby('Codigo de vecindad').plot(x=columna, y='Tiempo', logy=True, title=titulo)

plt.legend(labels, loc='upper left')
plt.ylabel('Tiempos de ejecucion (ms)')

sns.set_style("darkgrid")
plt.savefig("grafico.png")