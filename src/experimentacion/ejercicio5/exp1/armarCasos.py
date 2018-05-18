import numpy as np
from random import randint
import csv, commands, sys, math

path = "/home/laucha/Documentos/algo3segundocuatrimestre/"

param_amplitud = 2;
cant_casos = 5;
cant_nodos = 2.0;

archivo_salida = path + "tp3/src/experimentacion/ejercicio5/exp1/casos.in"

sys.stdout.write("------------------GENERA CASOS PARA EJ5 EXP1-----------------------\n")

num = 1
while cant_nodos <= 4000:

	sys.stdout.write("--- nodos: "+str(cant_nodos)+"\n")
	sys.stdout.flush()

	for num_caso in xrange(0,cant_casos):

		capacidad_mochila = 10
		cant_paradas = randint(math.ceil(cant_nodos/3), cant_nodos-1)
		cant_gimnasios = cant_nodos - cant_paradas
	
		sys.stdout.write("--- c: "+str(capacidad_mochila)+" - p: "+str(cant_paradas)+" - g: "+str(cant_gimnasios)+" - rep: "+str(num_caso)+"\n")
		sys.stdout.flush()
	
		#----Genero caso
		commands.getstatusoutput("python "+path+"tp3/src/experimentacion/generadorCasos.py "+archivo_salida+" "+str(int(cant_paradas))+" "+str(int(cant_gimnasios))+" "+str(int(capacidad_mochila))+" "+str(int(param_amplitud))+" 1 "+str(num)+" "+str(int(cant_nodos)))
		num += 1

	cant_nodos += math.ceil(cant_nodos / 40);
