import sys
import numpy as np
from random import randint


archivo_salida = sys.argv[1]
cant_paradas = int(sys.argv[2])
cant_gimnasios = int(sys.argv[3])
capacidad_mochila = int(sys.argv[4])
param_amplitud = int(sys.argv[5])

append = 0
if len(sys.argv) > 6:
	append = int(sys.argv[6])
codigo_caso = ""
if len(sys.argv) > 7:
	codigo_caso = sys.argv[7]
codigo_vecindad = ""
if len(sys.argv) > 8:
	codigo_vecindad = sys.argv[8]

if append == 1:
	f = open(archivo_salida, 'a')
else:
	f = open(archivo_salida, 'w')

#-----ESCRIBE CANTIDADES INICIALES
f.write(str(cant_gimnasios)+" "+str(cant_paradas)+" "+str(capacidad_mochila)+"\n")

#-----COMPLETA GIMNASIOS
cant_pociones_restantes = cant_paradas * 3
for i in xrange(1, cant_gimnasios+1):
	max_range = cant_pociones_restantes - (cant_gimnasios-i)
	if max_range > capacidad_mochila:
		max_range = capacidad_mochila
	cant_pociones = randint(1, max_range)
	cant_pociones_restantes = cant_pociones_restantes - cant_pociones

	nuevo_x = randint(1, cant_gimnasios * param_amplitud)
	nuevo_y = randint(1, cant_gimnasios * param_amplitud)

	f.write(str(nuevo_x)+" "+str(nuevo_y)+" "+str(cant_pociones)+"\n")

#-----COMPLETA PARADAS
for i in xrange(1, cant_paradas+1):

	nuevo_x = randint(1, cant_paradas * param_amplitud)
	nuevo_y = randint(1, cant_paradas * param_amplitud)

	f.write(str(nuevo_x)+" "+str(nuevo_y)+"\n")

if codigo_caso != "":
	f.write(codigo_caso)
	f.write("\n")
if codigo_vecindad != "":
	f.write(codigo_vecindad)
	f.write("\n")

f.write("\n")

f.close()