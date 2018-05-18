import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

#-------------------------------------------------------
#--  La idea es hacer 3 graficos mostrando el tiempo
#-- en funcion de la cantidad de paradas, la cantidad
#-- de gimnasios y la capacidad de la mochila
#-------------------------------------------------------

#----------FORMATO ESPERADO------------
#-- Codigo de caso
#-- Cantidad de gimnasios
#-- Cantidad de paradas
#-- Capacidad de la mochila
#-- Tiempo
#-- Distancia del camino
#-- Ejercicio

tipo = 'gimnasios'
columna = 'Cantidad de gimnasios'
if len(sys.argv) > 1:
	if sys.argv[1] == 'paradas':
		tipo = 'paradas'
		columna = 'Cantidad de paradas'
	elif sys.argv[1] == 'mochila':
		tipo = 'mochila'
		columna = 'Capacidad de la mochila'

titulo = str(columna)+" vs Tiempos de ejecucion (ms)"


nombres_programas = ['Heuristica golosa', 'Heurisita de busqueda local', 'Metaheuristica GRASP']

df = pd.read_csv('corrida.csv')

agrupado = df.groupby([columna, 'Ejercicio'], as_index=False).mean()

agrupado = agrupado.loc[agrupado['Ejercicio'] > 1]

agrupado[[columna, 'Ejercicio', 'Tiempo']].groupby('Ejercicio').plot(x=columna, y='Tiempo', logy=True, title=titulo)

plt.legend(nombres_programas, loc='upper left')
plt.ylabel('Tiempos de ejecucion (ms)')

sns.set_style("darkgrid")
#plt.show()
plt.savefig("grafico_"+str(tipo)+".png")