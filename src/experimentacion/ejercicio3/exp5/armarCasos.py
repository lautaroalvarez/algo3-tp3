import numpy as np
from random import randint
import csv, commands, sys, math

path = "/home/laucha/Documentos/algo3segundocuatrimestre/"

param_amplitud = 3;
cant_repeticiones = 5;
cant_casos = 100;

archivo_salida = path + "tp3/src/experimentacion/ejercicio3/exp5/casos.in"

max_cant_paradas = 11;
max_cant_gimnasios = 11;
maximo_capacidad = 7;

sys.stdout.write("------------------GENERA ARCHIVO DE RANDOM PARA EJ3-----------------------\n")


while cant_casos > 0:

	capacidad_mochila = randint(1, 7)
	cant_paradas = randint(1, 10)
	cant_gimnasios = randint(1, 10)
	
	sys.stdout.write("--- c: "+str(capacidad_mochila)+" - p: "+str(cant_paradas)+" - g: "+str(cant_gimnasios)+" - num caso: "+str(cant_casos)+"\n")
	sys.stdout.flush()
	
	#----Genero caso
	commands.getstatusoutput("python "+path+"tp3/src/experimentacion/generadorCasos.py "+archivo_salida+" "+str(int(cant_paradas))+" "+str(int(cant_gimnasios))+" "+str(int(capacidad_mochila))+" "+str(int(param_amplitud))+" 1 "+str(cant_casos))

	cant_casos -= 1;
