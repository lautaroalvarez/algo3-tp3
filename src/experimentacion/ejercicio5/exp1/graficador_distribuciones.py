import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys, math

#-------------------------------------------------------
#--  La idea de este grafico es agarrar caso por caso
#-- y ver el porcentaje de cercania de cada programa con
#-- la solucion exacta
#-------------------------------------------------------

#-----Lectura de entrada
df = pd.read_csv("corrida_completa.csv")

#-----Ajustes previos
df['Cantidad de nodos'] = df['Cantidad de gimnasios'] + df['Cantidad de paradas']
df = df.loc[df['Cantidad de nodos'] <= 20]

#--agrupa por esos dos campos y saca el promedio
agrupado = df.groupby(['Codigo de caso', 'Ejercicio'], as_index=False).mean()

#--ordena poniendo los 4 del mismo caso juntos y poniendo el que es exacto primero (esto para el ciclo que hago abajo)
agrupado = agrupado.sort(['Codigo de caso', 'Ejercicio'], ascending=True)

print agrupado

#--voy a recorrer todos los casos (porque esta ordenado asi)
#--primero me voy a encontrar con el algoritmo exacto, saco el valor_actual (resultado exacto)
#--despues comparo los 3 que siguen con esa variable valor_actual y calculo el porcentaje de error
valor_actual = -1
for i, row in agrupado.iterrows():
	#--si es el exacto me guardo el valor_actual
	if row['Ejercicio'] == 1:
		valor_actual = row['Distancia del camino']
	else:
		#--sino me fijo si el valor es 0 (algun caso raro) para que no divida por cero
		if valor_actual == 0:
			agrupado.loc[i,'Porcentaje de error'] = 0
		else:
			#--si es un caso normal saco el porcentaje del error y lo guardo en la columna "Porcentaje de error" de la fila actual
			agrupado.loc[i,'Porcentaje de error'] = 100 * math.fabs(valor_actual - row['Distancia del camino']) / math.fabs(valor_actual)


#--vamos a graficar las distribuciones de los porcentajes de error de cada programa

#--aca filtra que la distancia sea mayor a cero
#agrupado = agrupado.loc[agrupado['Distancia del camino'] > 0]

labels = ['Programa 2','Programa 3','Programa 4']
colores = ['red','green','blue','yellow']
titulo = 'Distribucion de los porcentajes de error por programa'

for ejercicio in xrange(2,5):
	agrupado_ejercicio = agrupado.loc[agrupado['Ejercicio'] == ejercicio]

	sns.kdeplot(agrupado_ejercicio['Porcentaje de error'], shade=True, color=colores[ejercicio-1]);

plt.legend(labels, loc='upper right')
plt.title(titulo)
plt.xlabel("Porcentaje de error")
plt.savefig('grafico_distribuciones.png')