import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys, math

#-------------------------------------------------------
#--  La idea de este grafico es agarrar caso por caso
#-- y ver el porcentaje de cercania de cada version con
#-- la solucion exacta. Tomar luego un valor de la
#-- relacion error-tiempo.
#-------------------------------------------------------

#----------FORMATO ESPERADO------------
#-- Codigo de caso
#-- Cantidad de gimnasios
#-- Cantidad de paradas
#-- Capacidad de la mochila
#-- Tiempo
#-- Distancia del camino
#-- Cantidad de cambios
#-- Codigo de vecindad

titulo = 'Relacion tiempos-calidad vs Cantidad de nodos'
labels = ['0001','0011','0111','1111']

#--se trae el csv
df = pd.read_csv("corrida_arreglada.csv")

#--agrupa por esos dos campos y saca el promedio, como son funciones y siempre dan el mismo resultado no me jode el promedio
agrupado = df.groupby(['Codigo de caso', 'Codigo de vecindad'], as_index=False).mean()

#--ordena poniendo los 4 del mismo caso juntos y poniendo el que es exacto primero (esto para el ciclo que hago abajo)
agrupado = agrupado.sort(['Codigo de caso', 'Codigo de vecindad'], ascending=False)

#--voy a recorrer todos los casos (porque esta ordenado asi)
#--primero me voy a encontrar con el algoritmo exacto, saco el valor_actual (resultado exacto)
#--despues comparo los 3 que siguen con esa variable valor_actual y calculo el porcentaje de error
valor_actual = -1
tiempo_actual = -1
for i, row in agrupado.iterrows():
	#--si es el exacto me guardo el valor_actual
	if row['Codigo de vecindad'] == " '2'":
		valor_actual = row['Distancia del camino']
		tiempo_actual = row['Tiempo']
	else:
		#--sino me fijo si el valor es 0 (algun caso raro) para que no divida por cero
		if valor_actual == 0:
			agrupado.loc[i,'Porcentaje de error'] = 0
		else:
			#--si es un caso normal saco el porcentaje del error y lo guardo en la columna "Porcentaje de error" de la fila actual
			agrupado.loc[i,'Porcentaje de error'] = 100 * math.fabs(valor_actual - row['Distancia del camino']) / math.fabs(valor_actual)
		agrupado.loc[i,'Porcentaje de tiempo'] = row['Tiempo'] * 100 / tiempo_actual

#-- armo una columna Cantidad de nodos
agrupado['Cantidad de nodos'] = agrupado['Cantidad de paradas'] + agrupado['Cantidad de gimnasios']

#---------TODOS LOS CASOS

todos = agrupado.groupby(['Cantidad de nodos','Codigo de vecindad'], as_index=False).mean()

todos['Relacion'] = 1 / (todos['Tiempo'] * todos['Porcentaje de error'])

#--elimino el caso del algoritmo exacto
todos = todos.loc[todos['Codigo de vecindad'] != " '2'"]

todos[['Cantidad de nodos', 'Codigo de vecindad', 'Relacion']].groupby('Codigo de vecindad').plot(x='Cantidad de nodos', y='Relacion', title=titulo)

plt.legend(labels, loc='upper left')
plt.ylabel('Tiempos de ejecucion (ms)')

sns.set_style("darkgrid")
plt.savefig("relaciones.png")



#--imprimo una tabla en formato latex con las columnas de "Codigo de vecindad" y "Porcentaje de error"
#print todos.to_latex(columns=['Codigo de vecindad', 'Porcentaje de error'])

#print ""

#--esto de abajo en lo mismo que el de arriba pero filtra los casos que sean validos (que la respuesta no sea -1)
#print "Casos validos"

#--aca filtra que la distancia sea mayor a cero
agrupado = agrupado.loc[agrupado['Distancia del camino'] > 0]

validos = agrupado.groupby(['Codigo de vecindad'], as_index=False).mean()

validos['Relacion'] = 100000 / (validos['Tiempo'] * validos['Porcentaje de error'])

validos = validos.loc[validos['Codigo de vecindad'] != " '2'"]

print validos.to_latex(columns=['Codigo de vecindad', 'Relacion'])



plt.clf()

validos = agrupado.groupby(['Cantidad de nodos','Codigo de vecindad'], as_index=False).mean()

validos[['Cantidad de nodos', 'Codigo de vecindad', 'Porcentaje de tiempo']].groupby('Codigo de vecindad').plot(x='Cantidad de nodos', y='Porcentaje de tiempo', title=titulo)

plt.legend(labels, loc='upper left')
plt.ylabel('Tiempos de ejecucion (ms)')

sns.set_style("darkgrid")
plt.show()


#--aca filtra que la distancia sea mayor a cero
agrupado = agrupado.loc[agrupado['Distancia del camino'] > 0]

validos_2 = agrupado.groupby(['Codigo de vecindad'], as_index=False).mean()

validos_2['Relacion'] = 100000 / (validos_2['Porcentaje de tiempo'] * validos_2['Porcentaje de error'])

validos_2 = validos_2.loc[validos_2['Codigo de vecindad'] != " '2'"]

print validos_2.to_latex(columns=['Codigo de vecindad', 'Relacion'])