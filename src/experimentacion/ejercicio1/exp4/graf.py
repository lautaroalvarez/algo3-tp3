import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

columna = 'Cantidad de paradas'

titulo = "Dispersion de los nodos vs Tiempos de ejecucion (ms)"

labels = ['Nodos muy dispersos', 'Nodos poco dispersos']

df = pd.read_csv("corrida.csv")

agrupado = df.groupby([columna, 'Mejor caso'], as_index=False).mean()

#agrupado = agrupado.loc[agrupado[columna] < 8]

agrupado[[columna, 'Mejor caso', 'Tiempo']].groupby('Mejor caso').plot(x=columna, y='Tiempo', logy=True, title=titulo)

plt.legend(labels, loc='upper left')
plt.ylabel('Tiempos de ejecucion (ms)')

sns.set_style("darkgrid")
#plt.show()
plt.savefig("grafico.png")
