import numpy as np
import csv, commands, sys, math

path = "/home/laucha/Documentos/algo3segundocuatrimestre/"

cant_repeticiones = 6;



#--------------------------------------------------------
archivo_salida = path + "tp3/src/experimentacion/ejercicio1/exp4/casos.in"
cant_gimnasios = 2;
maximo_paradas = 17;

sys.stdout.write("------------------GENERA ARCHIVO DE CASOS MEJORES CASOS-----------------------\n")
cant_paradas = 2;
while cant_paradas < maximo_paradas:
	for i in xrange(0,cant_repeticiones):
		sys.stdout.write("--- paradas: "+str(cant_paradas)+" rep: "+str(i)+"/"+str(cant_repeticiones)+"\n")
		sys.stdout.flush()
		
		commands.getstatusoutput("python "+path+"tp3/src/experimentacion/ejercicio1/generadorMejorCaso.py "+archivo_salida+" "+str(int(cant_paradas))+" "+str(int(cant_gimnasios))+" 1")

	cant_paradas += 1


sys.stdout.write("------------------GENERA ARCHIVO DE CASOS PEORES CASOS-----------------------\n")
cant_paradas = 2;
while cant_paradas < maximo_paradas:
	for i in xrange(0,cant_repeticiones):
		sys.stdout.write("--- paradas: "+str(cant_paradas)+" rep: "+str(i)+"/"+str(cant_repeticiones)+"\n")
		sys.stdout.flush()
		
		commands.getstatusoutput("python "+path+"tp3/src/experimentacion/ejercicio1/generadorPeorCaso.py "+archivo_salida+" "+str(int(cant_paradas))+" "+str(int(cant_gimnasios))+" 1")

	cant_paradas += 1

