import sys
import numpy as np
from random import randint

archivo_salida = sys.argv[1]
cant_gimnasios = int(sys.argv[2])
cant_paradas = int(sys.argv[3])
param_amplitud = 2
capacidad_mochila = 6

append = 0
if len(sys.argv) > 4:
	append = int(sys.argv[4])

if append == 1:
	f = open(archivo_salida, 'a')
else:
	f = open(archivo_salida, 'w')

gimnasios = np.empty((0,2))
paradas = np.empty((0,2))

#-----COMPLETA GIMNASIOS
for i in xrange(1, cant_gimnasios+1):
	nuevo_x = randint(1, cant_gimnasios * param_amplitud)
	nuevo_y = randint(1, cant_gimnasios * param_amplitud)
	gimnasios = np.append(gimnasios, np.array([[nuevo_x, nuevo_y]]), axis=0)

#-----COMPLETA PARADAS
for i in xrange(1, cant_paradas+1):
	nuevo_x = randint(1, cant_paradas * param_amplitud)
	nuevo_y = randint(1, cant_paradas * param_amplitud)
	paradas = np.append(paradas, np.array([[nuevo_x, nuevo_y]]), axis=0)

for pociones in xrange(0, 4):
	#-----ESCRIBE CANTIDADES INICIALES
	if pociones == 0:
		f.write(str(cant_gimnasios + cant_paradas - 1)+" 1 "+str(capacidad_mochila)+"\n")
	else:
		f.write(str(cant_gimnasios)+" "+str(cant_paradas)+" "+str(capacidad_mochila)+"\n")
	
	#-----ESCRIBE GIMNASIOS
	for gimnasio in gimnasios:
		f.write(str(int(gimnasio[0]))+" "+str(int(gimnasio[1]))+" "+str(pociones)+"\n")
	#-----ESCRIBE PARADAS
	cont = 1
	for parada in paradas:
		if pociones == 0 and cont < cant_paradas:
			#--escribo como si fuera un gimnasio (el ultimo lo escribe como parada)
			f.write(str(int(parada[0]))+" "+str(int(parada[1]))+" 0\n")
		else:
			f.write(str(int(parada[0]))+" "+str(int(parada[1]))+"\n")
		cont += 1
	#-----ESCRIBE LA CANTIDAD DE POCIONES
	f.write(str(pociones)+"\n")
	f.write("\n")

f.close()
