import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

#-----Lectura de entrada
df = pd.read_csv("corrida_completa.csv")

#-----Ajustes previos
df['Cantidad de nodos'] = df['Cantidad de gimnasios'] + df['Cantidad de paradas']
#labels = ['Algoritmo Exacto', 'Heuristica Golosa', 'Heuristica de Busqueda Local', 'Metaheuristica']
labels = ['Programa 1', 'Programa 2', 'Programa 3', 'Programa 4']
colores = ['red','green','blue','yellow']
labelx = 'Cantidad de nodos'
labely = 'Tiempos de ejecucion (ms)'



#-----GRAFICO DE COMPLEJIDAD HASTA 20 NODOS --- TODOS LOS ALGORITMOS
titulo = "Cantidad de nodos vs Tiempos de ejecucion (ms)"

plt.clf()
fig, ax = plt.subplots()

agrupado = df.loc[df['Cantidad de nodos'] <= 20].groupby('Ejercicio')

for name, group in agrupado:
	ax.scatter(group['Cantidad de nodos'], group['Tiempo'], c=colores[name-1], label=labels[name-1])

ax.set_yscale('log')

ax.set_xlim(xmin=1.0)
ax.set_xlim(xmax=21.0)
ax.set_ylim(ymin=0.1)


# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.title(titulo)
plt.xlabel(labelx)
plt.ylabel(labely)

plt.savefig("grafico_complejidad_hasta_20.png")





#-----GRAFICO DE COMPLEJIDAD HASTA 200 NODOS --- ALGORITMOS 2, 3 y 4
titulo = "Cantidad de nodos vs Tiempos de ejecucion (ms)"

plt.clf()
fig, ax = plt.subplots()

agrupado = df.loc[ (df['Cantidad de nodos'] <= 200) & (df['Ejercicio'] != 1) ].groupby('Ejercicio')

for name, group in agrupado:
	if name == 3:
		print group['Tiempo'].describe()
	ax.scatter(group['Cantidad de nodos'], group['Tiempo'], c=colores[name-1], label=labels[name-1])

ax.set_yscale('log', basey=10)

ax.set_xlim(xmin=1.0)
ax.set_xlim(xmax=201.0)
ax.set_ylim(ymin=0.1)

# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.title(titulo)
plt.xlabel(labelx)
plt.ylabel(labely)

plt.savefig("grafico_complejidad_hasta_200.png")






#-----GRAFICO DE COMPLEJIDAD HASTA 1000 NODOS --- ALGORITMOS 2 y 3
titulo = "Cantidad de nodos vs Tiempos de ejecucion (ms)"

plt.clf()
fig, ax = plt.subplots()

agrupado = df.loc[ (df['Cantidad de nodos'] <= 1000) & (df['Ejercicio'] != 1) & (df['Ejercicio'] != 4) ].groupby('Ejercicio')

for name, group in agrupado:
	ax.scatter(group['Cantidad de nodos'], group['Tiempo'], c=colores[name-1], label=labels[name-1])

ax.set_yscale('log')

ax.set_xlim(xmin=1.0)
ax.set_xlim(xmax=1001.0)
ax.set_ylim(ymin=0.1)


# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.title(titulo)
plt.xlabel(labelx)
plt.ylabel(labely)

plt.savefig("grafico_complejidad_hasta_1000.png")







#___________A PARTIR DE AHORA SOLO CASOS VALIDOS______




#-----GRAFICO DE COMPLEJIDAD HASTA 20 NODOS --- TODOS LOS ALGORITMOS
titulo = "Cantidad de nodos vs Tiempos de ejecucion (ms)"

plt.clf()
fig, ax = plt.subplots()

agrupado = df.loc[ (df['Cantidad de nodos'] <= 20) & (df['Distancia del camino'] > 0) ].groupby('Ejercicio')

for name, group in agrupado:
	ax.scatter(group['Cantidad de nodos'], group['Tiempo'], c=colores[name-1], label=labels[name-1])

ax.set_yscale('log')

ax.set_xlim(xmin=1.0)
ax.set_xlim(xmax=21.0)
ax.set_ylim(ymin=0.1)


# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.title(titulo)
plt.xlabel(labelx)
plt.ylabel(labely)

plt.savefig("grafico_complejidad_hasta_20_validos.png")





#-----GRAFICO DE COMPLEJIDAD HASTA 200 NODOS --- ALGORITMOS 2, 3 y 4
titulo = "Cantidad de nodos vs Tiempos de ejecucion (ms)"

plt.clf()
fig, ax = plt.subplots()

agrupado = df.loc[ (df['Cantidad de nodos'] <= 200) & (df['Distancia del camino'] > 0) & (df['Ejercicio'] != 1) ].groupby('Ejercicio')

for name, group in agrupado:
	ax.scatter(group['Cantidad de nodos'], group['Tiempo'], c=colores[name-1], label=labels[name-1])

ax.set_yscale('log')

ax.set_xlim(xmin=1.0)
ax.set_xlim(xmax=201.0)
ax.set_ylim(ymin=0.1)


# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.title(titulo)
plt.xlabel(labelx)
plt.ylabel(labely)

plt.savefig("grafico_complejidad_hasta_200_validos.png")






#-----GRAFICO DE COMPLEJIDAD HASTA 1000 NODOS --- ALGORITMOS 2 y 3
titulo = "Cantidad de nodos vs Tiempos de ejecucion (ms)"

plt.clf()
fig, ax = plt.subplots()

agrupado = df.loc[ (df['Cantidad de nodos'] <= 1000) & (df['Distancia del camino'] > 0) & (df['Ejercicio'] != 1) & (df['Ejercicio'] != 4) ].groupby('Ejercicio')

for name, group in agrupado:
	ax.scatter(group['Cantidad de nodos'], group['Tiempo'], c=colores[name-1], label=labels[name-1])

ax.set_yscale('log')

ax.set_xlim(xmin=1.0)
ax.set_xlim(xmax=1001.0)
ax.set_ylim(ymin=0.1)


# Shrink current axis by 20%
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

# Put a legend to the right of the current axis
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.title(titulo)
plt.xlabel(labelx)
plt.ylabel(labely)

plt.savefig("grafico_complejidad_hasta_1000_validos.png")



