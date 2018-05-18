import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

titulo = "Distancia del camino vs epocas"

df = pd.read_csv("corrida.csv")

df[['Cantidad de cambios', 'Distancia del camino']].plot(x='Cantidad de cambios', y='Distancia del camino', title=titulo)

plt.ylabel('Distancia del camino')
plt.xlabel('Epoca')
plt.ylim(0,900)

sns.set_style("darkgrid")
plt.savefig("grafico.png")