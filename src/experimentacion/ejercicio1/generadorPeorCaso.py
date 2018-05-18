import sys, math
import numpy as np
from random import randint

archivo_salida = sys.argv[1]
cant_paradas = int(sys.argv[2])
cant_gimnasios = int(sys.argv[3])
capacidad_mochila = 6
pociones_gimnasio = 3

append = 0
if len(sys.argv) > 4:
	append = int(sys.argv[4])

if append == 1:
	f = open(archivo_salida, 'a')
else:
	f = open(archivo_salida, 'w')

#-----ESCRIBE CANTIDADES INICIALES
f.write(str(cant_gimnasios)+" "+str(cant_paradas)+" "+str(capacidad_mochila)+"\n")

#-----COMPLETA GIMNASIOS
radio = int(round(math.sqrt(cant_gimnasios + cant_paradas) / 2))
indice = 0
for i in xrange(1, cant_gimnasios+1):

	fila_colum = indice / (radio * 2)
	index = indice % (radio * 2)
	if fila_colum == 0:
		nuevo_x = -radio + index
		nuevo_y = -radio
	elif fila_colum == 1:
		nuevo_x = radio
		nuevo_y = -radio + index
	elif fila_colum == 2:
		nuevo_x = radio - index
		nuevo_y = radio
	elif fila_colum == 3:
		nuevo_x = -radio
		nuevo_y = radio - index

	indice += 1
	if indice == radio * 2 * 4:
		indice = 0
		radio -= 1

	f.write(str(nuevo_x)+" "+str(nuevo_y)+" "+str(pociones_gimnasio)+"\n")

#-----COMPLETA PARADAS
for i in xrange(1, cant_paradas+1):

	fila_colum = indice / (radio * 2)
	index = indice % (radio * 2)
	if fila_colum == 0:
		nuevo_x = -radio + index
		nuevo_y = -radio
	elif fila_colum == 1:
		nuevo_x = radio
		nuevo_y = -radio + index
	elif fila_colum == 2:
		nuevo_x = radio - index
		nuevo_y = radio
	elif fila_colum == 3:
		nuevo_x = -radio
		nuevo_y = radio - index

	indice += 1
	if indice == radio * 2 * 4:
		indice = 0
		radio -= 1


	f.write(str(nuevo_x)+" "+str(nuevo_y)+"\n")

#--marca de peor caso (=0)
f.write("0\n")

f.write("\n")

f.close()