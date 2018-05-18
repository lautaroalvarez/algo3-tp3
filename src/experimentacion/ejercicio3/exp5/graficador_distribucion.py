import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys, math

#-------------------------------------------------------
#--  La idea de este grafico es agarrar caso por caso
#-- y ver el porcentaje de cercania de cada version con
#-- la solucion exacta
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
for i, row in agrupado.iterrows():
	#--si es el exacto me guardo el valor_actual
	if row['Codigo de vecindad'] == " '2'":
		valor_actual = row['Distancia del camino']
	else:
		#--sino me fijo si el valor es 0 (algun caso raro) para que no divida por cero
		if valor_actual == 0:
			agrupado.loc[i,'Porcentaje de error'] = 0
		else:
			#--si es un caso normal saco el porcentaje del error y lo guardo en la columna "Porcentaje de error" de la fila actual
			agrupado.loc[i,'Porcentaje de error'] = 100 * math.fabs(valor_actual - row['Distancia del camino']) / math.fabs(valor_actual)




#--vamos a graficar las distribuciones de los porcentajes de error de cada version del programa

#--aca filtra que la distancia sea mayor a cero
agrupado = agrupado.loc[agrupado['Distancia del camino'] > 0]

tipos = ['0001', '0011', '0111', '1111']

for tipo in tipos:
	agrupado_tipo = agrupado.loc[agrupado['Codigo de vecindad'] == " '"+tipo+"'"]

	sns.kdeplot(agrupado_tipo['Porcentaje de error'], shade=True);

plt.legend(tipos, loc='upper right')
plt.xlabel("Porcentaje de error")
plt.savefig('distribuciones.png')