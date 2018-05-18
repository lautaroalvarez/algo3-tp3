import matplotlib.pyplot as plt
import sys, csv, math
import numpy as np
import seaborn as sns

#-------------------------------------------------------
#--  La idea de este grafico es agarrar caso por caso
#-- y ver quien estuvo mas cerca. Se suma 1 punto por
#-- cada caso ganado.
#-------------------------------------------------------

#----------FORMATO ESPERADO------------
#-- Codigo de caso
#-- Cantidad de gimnasios
#-- Cantidad de paradas
#-- Capacidad de la mochila
#-- Tiempo
#-- Distancia del camino
#-- Ejercicio



nombres_programas = np.array(['Algorimto exacto', 'Heuristica golosa', 'Heurisita de busqueda local', 'Metaheuristica GRASP', 'Sin ganador'])
colores_programas = np.array(['yellow', 'red', 'green', 'blue', 'gray'])

cantidad_total = 0
ganadas_por_ej = np.array([0, 0, 0, 0, 0])
resultado_por_ej = np.array([-1,-1,-1,-1])

entrada = csv.reader(open("corrida.csv", "rb"))

primera_fila = 1
caso_actual = -1
datos_actual = np.empty((0))

for row in entrada:
	if primera_fila == 1:
		primera_fila = 0
	else:
		if caso_actual != int(row[0]):
			if caso_actual != -1:
				ej_ganador = np.array([4])
				min = -1
				for i in xrange(1,4):
					diff = math.fabs(resultado_por_ej[i] - resultado_por_ej[0])
					if resultado_por_ej[i] >= 0 and (min == -1 or diff <= min):
						if diff == min:
							ej_ganador = np.append(ej_ganador, np.array([i]), axis=0)
						else:
							min = diff
							ej_ganador = np.array([i])
				for i in xrange(0,len(ej_ganador)):
					ganadas_por_ej[ej_ganador[i]] += 1
				cantidad_total += 1

			caso_actual = int(row[0])
			resultado_por_ej = np.array([-1,-1,-1,-1])

		if float(row[5]) >= 0 and (resultado_por_ej[int(row[6])-1] == -1 or resultado_por_ej[int(row[6])-1] > float(row[5])):
			resultado_por_ej[int(row[6])-1] = float(row[5])

if caso_actual != -1:
	ej_ganador = np.array([4])
	min = -1
	for i in xrange(1,4):
		diff = math.fabs(resultado_por_ej[i] - resultado_por_ej[0])
		if resultado_por_ej[i] >= 0 and (min == -1 or diff <= min):
			if diff == min:
				ej_ganador = np.append(ej_ganador, np.array([i]), axis=0)
			else:
				min = diff
				ej_ganador = np.array([i])
	for i in xrange(0,len(ej_ganador)):
		ganadas_por_ej[ej_ganador[i]] += 1
	cantidad_total += 1


sns.barplot(nombres_programas[1:], ganadas_por_ej[1:], color=colores_programas[1:])

labelx = "Algoritmo"
labely = "Cantidad de soluciones"
titulo = "Cantidad de soluciones mas cercanas [Cantidad total = "+str(cantidad_total)+"]"

plt.xlabel(labelx)
plt.ylabel(labely)
plt.title(titulo)
#plt.legend(nombres_programas[1:], loc='upper left')

sns.set_style("darkgrid")

#plt.show()
plt.savefig("grafico1.png")