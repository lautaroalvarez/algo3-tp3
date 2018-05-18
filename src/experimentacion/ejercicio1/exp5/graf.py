import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys

#-------------- GRAFICO LINEAS (tiempos de ejecucion) -----------------
columna = 'Cantidad de nodos'

titulo = "Pociones en gimnasios - TSP vs no-TSP"

labels = ['0 (TSP)', '1', '2', '3']

df = pd.read_csv("corrida.csv")

df['Cantidad de nodos'] = df['Cantidad de paradas'] + df['Cantidad de gimnasios']

agrupado = df.groupby([columna, 'Pociones Gimnasio'], as_index=False).mean()

#agrupado = agrupado.loc[agrupado[columna] < 8]

agrupado[[columna, 'Pociones Gimnasio', 'Tiempo']].groupby('Pociones Gimnasio').plot(x=columna, y='Tiempo', logy=True, title=titulo)

plt.legend(labels, loc='upper left')
plt.ylabel('Tiempos de ejecucion (ms)')

sns.set_style("darkgrid")
#plt.show()
plt.savefig("grafico.png")



#-------------- TABLA DATOS (tsp vs 3) -----------------

agrupado = agrupado.loc[ (agrupado['Pociones Gimnasio'] != 1) & (agrupado['Pociones Gimnasio'] != 2) ]

#print agrupado

print "\\begin{tabular}{| c | c | c | c | c | c | c | c | c |}"
print "  \hline"
print "  Cantidad de nodos & \multicolumn{2}{|c|}{Instancias visitadas} & \multicolumn{2}{|c|}{Instancias calculadas} & \multicolumn{2}{|c|}{Cantidad de podas tipo 1} & \multicolumn{2}{|c|}{Cantidad de podas tipo 2} \\\\"
print "   & TSP & no-TSP & TSP & no-TSP & TSP & no-TSP & TSP & no-TSP \\\\ \cline{2-8}"
print "  2 & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\\\"
print "  \hline"
print "\end{tabular}"

print "\n"

agrupado['Pociones Gimnasio'] = np.where(agrupado['Pociones Gimnasio'] == 0, '0 (TSP)', '3')

print agrupado.to_latex(columns=['Cantidad de nodos', 'Pociones Gimnasio', 'Cantidad de instancias visitadas', 'Cantidad de instancias calculadas', 'Cantidad de podas 1', 'Cantidad de podas 2'])

#print "\\begin{tabular}{|c|c|c|c|c|c|}"
#print "\hline"
#print " Cantidad de nodos &  & Instancias visitadas & Instancias calculadas & Cantidad de podas tipo 1 & Cantidad de podas tipo 2 \\\\ \hline"
#for i in agrupado:
#	print " "+str(fila['Cantidad de nodos'])+" & "+str(fila['Pociones Gimnasio'])+" & "+str(fila['Cantidad de instancias visitadas'])+" & "+str(fila['Cantidad de instancias calculadas'])+" & "+str(fila['Cantidad de podas 1'])+" & "+str(fila['Cantidad de podas 2'])+" \\\\ \hline"
#print " \end{tabular}"