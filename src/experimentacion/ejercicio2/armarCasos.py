import numpy as np
import csv, commands, sys, math

path = "/home/matias/algo3segundocuatrimestre/"

param_amplitud = 2;
cant_repeticiones = 1;


#--------------------------------------------------------
#archivo_salida = path + "tp3/src/experimentacion/ejercicio3/exp1/casos.in"
#cant_gimnasios = 5;
#capacidad_mochila = 5;
#maximo_paradas = 1000;
#
#sys.stdout.write("------------------GENERA ARCHIVO DE CASOS AUMENTANDO PARADAS-----------------------\n")
#
#cant_paradas = 2;
#while cant_paradas < maximo_paradas:
#
#	for i in xrange(0,cant_repeticiones):
#			
#		sys.stdout.write("--- paradas: "+str(cant_paradas)+" rep: "+str(i)+"/"+str(cant_repeticiones)+"\n")
#		sys.stdout.flush()
#		
#		#----Genero caso
#		commands.getstatusoutput("python "+path+"tp3/src/experimentacion/generadorCasos.py "+archivo_salida+" "+str(int(cant_paradas))+" "+str(int(cant_gimnasios))+" "+str(int(capacidad_mochila))+" "+str(int(param_amplitud))+" 1 "+str(cant_gimnasios)+"_"+str(cant_paradas)+"_"+str(capacidad_mochila)+"_"+str(i))
#
#	cant_paradas += 1




#--------------------------------------------------------
archivo_salida = path + "tp3/src/experimentacion/ejercicio2/exp2/casos.in"
cant_paradas = 1500;
capacidad_mochila = 200;
cant_gimnasios = 50;

sys.stdout.write("------------------GENERA ARCHIVO DE CASOS AUMENTANDO GIMNASIOS-----------------------\n")

while cant_paradas > 0:

	for i in xrange(0,cant_repeticiones):
		
		sys.stdout.write("--- gimnasios: "+str(cant_gimnasios)+" rep: "+str(i)+"/"+str(cant_repeticiones)+"\n")
		sys.stdout.flush()
		
		#----Genero caso
		commands.getstatusoutput("python "+path+"tp3/src/experimentacion/generadorCasos.py "+archivo_salida+" "+str(int(cant_paradas))+" "+str(int(cant_gimnasios))+" "+str(int(capacidad_mochila))+" "+str(int(param_amplitud))+" 1 "+str(cant_gimnasios)+"_"+str(cant_paradas)+"_"+str(capacidad_mochila)+"_"+str(i))

	cant_paradas -= 10





#--------------------------------------------------------
#archivo_salida = path + "tp3/src/experimentacion/ejercicio3/exp3/casos.in"
#cant_paradas = 5;
#cant_gimnasios = 6;
#maximo_capacidad = 1000;
#
#sys.stdout.write("------------------GENERA ARCHIVO DE CASOS AUMENTANDO MOCHILA-----------------------\n")
#
#capacidad_mochila = 2;
#while capacidad_mochila < maximo_capacidad:
#
#	for i in xrange(0,cant_repeticiones):
#		
#		sys.stdout.write("--- mochila: "+str(capacidad_mochila)+" rep: "+str(i)+"/"+str(cant_repeticiones)+"\n")
#		sys.stdout.flush()
#		
#		#----Genero caso
#		commands.getstatusoutput("python "+path+"tp3/src/experimentacion/generadorCasos.py "+archivo_salida+" "+str(int(cant_paradas))+" "+str(int(cant_gimnasios))+" "+str(int(capacidad_mochila))+" "+str(int(param_amplitud))+" 1 "+str(cant_gimnasios)+"_"+str(cant_paradas)+"_"+str(capacidad_mochila)+"_"+str(i))
#
#	capacidad_mochila += 1
