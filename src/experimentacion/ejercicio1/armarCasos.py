import numpy as np
import csv, commands, sys, math

path = "/home/laucha/Documentos/algo3segundocuatrimestre/"

param_amplitud = 2;
cant_repeticiones = 8;




#--------------------------------------------------------
archivo_salida = path + "tp3/src/experimentacion/ejercicio1/casos1.in"
cant_gimnasios = 3;
capacidad_mochila = 5;
maximo_paradas = 16;

sys.stdout.write("------------------GENERA ARCHIVO DE CASOS AUMENTANDO PARADAS-----------------------\n")

cant_paradas = 15;
while cant_paradas < maximo_paradas:
	for i in xrange(0,cant_repeticiones):
		sys.stdout.write("--- paradas: "+str(cant_paradas)+" rep: "+str(i)+"/"+str(cant_repeticiones)+"\n")
		sys.stdout.flush()
		
		#----Genero caso
		commands.getstatusoutput("python "+path+"tp3/src/experimentacion/generadorCasos.py "+archivo_salida+" "+str(int(cant_paradas))+" "+str(int(cant_gimnasios))+" "+str(int(capacidad_mochila))+" "+str(int(param_amplitud))+" 1")

	cant_paradas += 1




#--------------------------------------------------------
archivo_salida = path + "tp3/src/experimentacion/ejercicio1/casos2.in"
cant_paradas = 4;
capacidad_mochila = 4;
maximo_gimnasios = 11;

sys.stdout.write("------------------GENERA ARCHIVO DE CASOS AUMENTANDO GIMNASIOS-----------------------\n")

cant_gimnasios = 10;
while cant_gimnasios < maximo_gimnasios:
	for i in xrange(0, cant_repeticiones):
		sys.stdout.write("--- gimnasios: "+str(cant_gimnasios)+" rep: "+str(i)+"/"+str(cant_repeticiones)+"\n")
		sys.stdout.flush()
		
		#----Genero caso
		commands.getstatusoutput("python "+path+"tp3/src/experimentacion/generadorCasos.py "+archivo_salida+" "+str(int(cant_paradas))+" "+str(int(cant_gimnasios))+" "+str(int(capacidad_mochila))+" "+str(int(param_amplitud))+" 1")

	cant_gimnasios += 1





#--------------------------------------------------------
archivo_salida = path + "tp3/src/experimentacion/ejercicio1/casos3.in"
cant_paradas = 4;
cant_gimnasios = 4;
maximo_capacidad = 11;

sys.stdout.write("------------------GENERA ARCHIVO DE CASOS AUMENTANDO MOCHILA-----------------------\n")

capacidad_mochila = 10;
while capacidad_mochila < maximo_capacidad:
	for i in xrange(0, cant_repeticiones):
		sys.stdout.write("--- capacidad: "+str(capacidad_mochila)+" rep: "+str(i)+"/"+str(cant_repeticiones)+"\n")
		sys.stdout.flush()
		
		#----Genero caso
		commands.getstatusoutput("python "+path+"tp3/src/experimentacion/generadorCasos.py "+archivo_salida+" "+str(int(cant_paradas))+" "+str(int(cant_gimnasios))+" "+str(int(capacidad_mochila))+" "+str(int(param_amplitud))+" 1")

	capacidad_mochila += 1
