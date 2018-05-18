import matplotlib.pyplot as plt
import sys, csv, math
import numpy as np
import seaborn as sns

#----------FORMATO ESPERADO------------
#-- cantidad gimnasios
#-- cantidad paradas
#-- capacidad mochila
#-- repeticion
#-- tiempo total
#-- cantidad de instancias que visito
#-- cantidad de instancias que calculo
#-- tamano del camino solucion
#-- version de algoritmo (podas)
#-- cantidad de podas 1
#-- cantidad de podas 2

tipo = "tiempos"
if len(sys.argv) > 1:
	tipo = sys.argv[1]


nombres_versiones = np.array(['Version 0', 'Version 1', 'Version 2', 'Version 3', 'Version 4'])
archivos_versiones = np.array(['version0.csv', 'version1.csv', 'version2.csv', 'version3.csv', 'version4.csv'])
colores_versiones = np.array(['red', 'yellow', 'green', 'black', 'blue'])

labelx = "Cantidad de gimnasios"
labely = "Tiempo de ejecucion (ms)"
titulo = "Cantidad de gimnasios vs Tiempo de ejecucion"

columna_medicion = 4
if tipo == "instancias_visitadas":
	columna_medicion = 6
	labely = "Cantidad de instancias visitadas"
	titulo = "Cantidad de instancias visitadas vs Tiempo de ejecucion"
elif tipo == "instancias_calculadas":
	columna_medicion = 7
	labely = "Cantidad de instancias calculadas"
	titulo = "Cantidad de instancias calculadas vs Tiempo de ejecucion"
elif tipo == "podas":
	columna_medicion = 9
	labely = "Cantidad de podas"
	titulo = "Cantidad de podas vs Tiempo de ejecucion"

columna_dato = 0
desde = 1

maximo = 0;

for i in xrange(desde, len(nombres_versiones)):
	
	ejex = np.empty((0))
	ejey = np.empty((0))
	
	entrada = csv.reader(open(archivos_versiones[i], "rb"))

	primera_fila = 1
	gimnasios_actual = -1
	datos_actual = np.empty((0))
	for row in entrada:
		if primera_fila == 1:
			primera_fila = 0
		else:
			if gimnasios_actual != row[columna_dato]:
				if gimnasios_actual != -1:
					datos_actual = np.delete(datos_actual, np.argmax(datos_actual))
					datos_actual = np.delete(datos_actual, np.argmin(datos_actual))
					ejex = np.append(ejex, np.array([gimnasios_actual]), axis=0)
					promedio = np.mean(datos_actual)
					if promedio > maximo:
						maximo = promedio
					ejey = np.append(ejey, np.array([promedio]), axis=0)
				gimnasios_actual = row[columna_dato]
				datos_actual = np.empty((0))
		
			if columna_medicion == 9:
				datos_actual = np.append(datos_actual, [float(row[9])+float(row[10])])
			else:
				datos_actual = np.append(datos_actual, [float(row[columna_medicion])])

	if gimnasios_actual!=-1:
		datos_actual = np.delete(datos_actual, np.argmax(datos_actual))
		datos_actual = np.delete(datos_actual, np.argmin(datos_actual))
		ejex = np.append(ejex, np.array([gimnasios_actual]), axis=0)
		promedio = np.mean(datos_actual)
		if promedio > maximo:
			maximo = promedio
		ejey = np.append(ejey, np.array([promedio]), axis=0)
	
	plt.plot(ejex, ejey, color=colores_versiones[i])


x1,x2,y1,y2 = plt.axis()
plt.axis((x1-1,x2+1,0,maximo * 1.05))

plt.xlabel(labelx)
plt.ylabel(labely)
plt.title(titulo)
plt.legend(nombres_versiones[desde:], loc='upper left')

sns.set_style("darkgrid")

#plt.show()
plt.savefig("salida_"+str(tipo)+".png")