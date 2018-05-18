import numpy as np
import csv, commands, sys, math

path = "/home/laucha/Documentos/algo3segundocuatrimestre/"

cant_repeticiones = 2;


#--------------------------------------------------------
archivo_salida = path + "tp3/src/experimentacion/ejercicio1/exp5/casos.in"
maximo_nodos = 20

sys.stdout.write("------------------GENERA ARCHIVO DE CASOS MEJORES CASOS-----------------------\n")
cant_nodos = 4;
while cant_nodos < maximo_nodos:
	for i in xrange(0, cant_repeticiones):
		sys.stdout.write("--- nodos: "+str(cant_nodos)+" rep: "+str(i)+"/"+str(cant_repeticiones)+"\n")
		sys.stdout.flush()

		commands.getstatusoutput("python "+path+"tp3/src/experimentacion/ejercicio1/generadorTsp.py "+archivo_salida+" "+str(int(cant_nodos / 2))+" "+str(int(cant_nodos / 2))+" 1")

	cant_nodos += 2