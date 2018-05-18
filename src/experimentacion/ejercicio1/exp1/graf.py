import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

#pd.set_option('display.precision',20)

columna = 'Cantidad de paradas'

titulo = str(columna)+" vs Tiempos de ejecucion (ms)"

nombres_versiones = ['Version 0', 'Version 1', 'Version 2', 'Version 3', 'Version 4']
archivos_versiones = ['version0.csv', 'version1.csv', 'version2.csv', 'version3.csv', 'version4.csv']
#archivos_versiones = ['version4.csv']

df = pd.read_csv(archivos_versiones[0])

for i in xrange(1, len(archivos_versiones)):
	dfn = pd.read_csv(archivos_versiones[i])
	df = pd.concat([df, dfn])

agrupado = df.groupby([columna, 'Version de podas'], as_index=False).mean()

#agrupado = agrupado.loc[agrupado['Version de podas'] > 0].loc[agrupado['Cantidad de paradas'] > 9]

agrupado[[columna, 'Version de podas', 'Tiempo']].groupby('Version de podas').plot(x=columna, y='Tiempo', logy=True, title=titulo)

plt.legend(nombres_versiones, loc='upper left')
#plt.legend(nombres_versiones[1:], loc='upper left')
plt.ylabel('Tiempos de ejecucion (ms)')

sns.set_style("darkgrid")
#plt.show()
plt.savefig("grafico.png")
#plt.savefig("grafico_2.png")