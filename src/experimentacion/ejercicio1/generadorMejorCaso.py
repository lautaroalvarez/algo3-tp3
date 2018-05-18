import sys
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
radio_cercano = 1
indice_cercano = 0
for i in xrange(1, cant_gimnasios+1):

	fila_colum = indice_cercano / (radio_cercano * 2)
	index = indice_cercano % (radio_cercano * 2)
	if fila_colum == 0:
		nuevo_x = -radio_cercano + index
		nuevo_y = -radio_cercano
	elif fila_colum == 1:
		nuevo_x = radio_cercano
		nuevo_y = -radio_cercano + index
	elif fila_colum == 2:
		nuevo_x = radio_cercano - index
		nuevo_y = radio_cercano
	elif fila_colum == 3:
		nuevo_x = -radio_cercano
		nuevo_y = radio_cercano - index

	indice_cercano += 1
	if indice_cercano == radio_cercano * 2 * 4:
		indice_cercano = 0
		radio_cercano += 1

	f.write(str(nuevo_x)+" "+str(nuevo_y)+" "+str(pociones_gimnasio)+"\n")

#-----COMPLETA PARADAS
cant_paradas_cercanas = cant_gimnasios
radio_lejano = radio_cercano * 200
indice_lejano = 0
for i in xrange(1, cant_paradas+1):

	if cant_paradas_cercanas > 0:

		#-----lo pongo cerca de los gimnasios
		fila_colum = indice_cercano / (radio_cercano * 2)
		index = indice_cercano % (radio_cercano * 2)
		if fila_colum == 0:
			nuevo_x = -radio_cercano + index
			nuevo_y = -radio_cercano
		elif fila_colum == 1:
			nuevo_x = radio_cercano
			nuevo_y = -radio_cercano + index
		elif fila_colum == 2:
			nuevo_x = radio_cercano - index
			nuevo_y = radio_cercano
		elif fila_colum == 3:
			nuevo_x = -radio_cercano
			nuevo_y = radio_cercano - index

		indice_cercano += 1
		if indice_cercano == radio_cercano * 2 * 4:
			indice_cercano = 0
			radio_cercano += 1
		
	else:
		#-----lo pongo muy lejos de los gimnasios
		fila_colum = indice_lejano / (radio_lejano * 2)
		index = indice_lejano % (radio_lejano * 2)
		if fila_colum == 0:
			nuevo_x = -radio_lejano + index
			nuevo_y = -radio_lejano
		elif fila_colum == 1:
			nuevo_x = radio_lejano
			nuevo_y = -radio_lejano + index
		elif fila_colum == 2:
			nuevo_x = radio_lejano - index
			nuevo_y = radio_lejano
		elif fila_colum == 3:
			nuevo_x = -radio_lejano
			nuevo_y = radio_lejano - index

		indice_lejano += 1
		if indice_lejano == radio_lejano * 2 * 4:
			indice_lejano = 0
			radio_lejano += 1

	cant_paradas_cercanas -= 1

	f.write(str(nuevo_x)+" "+str(nuevo_y)+"\n")

#--marca de mejor caso (=1)
f.write("1\n")

f.write("\n")

f.close()