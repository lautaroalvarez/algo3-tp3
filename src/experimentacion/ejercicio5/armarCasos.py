import numpy as np
import csv, commands, sys, math

path = "/home/laucha/Documentos/algo3segundocuatrimestre/"

param_amplitud = 3;
cant_repeticiones = 8;

archivo_salida = path + "tp3/src/experimentacion/ejercicio5/casos.in"

max_cant_paradas = 10;
max_cant_gimnasios = 10;
maximo_capacidad = 7;

sys.stdout.write("------------------GENERA ARCHIVO DE TODO TIPO PARA EJ5-----------------------\n")

capacidad_mochila = 1;
while capacidad_mochila < maximo_capacidad:
	cant_paradas = 1;
	while cant_paradas < max_cant_paradas:
		cant_gimnasios = 1;
		while cant_gimnasios < max_cant_gimnasios:
			for i in xrange(0, cant_repeticiones):
				sys.stdout.write("--- c: "+str(capacidad_mochila)+" - p: "+str(cant_paradas)+" - g: "+str(cant_gimnasios)+" - rep: "+str(i)+"/"+str(cant_repeticiones)+"\n")
				sys.stdout.flush()
				
				#----Genero caso
				commands.getstatusoutput("python "+path+"tp3/src/experimentacion/generadorCasos.py "+archivo_salida+" "+str(int(cant_paradas))+" "+str(int(cant_gimnasios))+" "+str(int(capacidad_mochila))+" "+str(int(param_amplitud))+" 1 "+str(cant_gimnasios)+"_"+str(cant_paradas)+"_"+str(capacidad_mochila)+"_"+str(i))
			cant_gimnasios += 1;
		cant_paradas += 1;
	capacidad_mochila += 1;
