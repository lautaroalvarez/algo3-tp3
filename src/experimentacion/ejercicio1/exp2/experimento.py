import numpy as np
import csv, commands, sys

path = "/home/laucha/Documentos/algo3segundocuatrimestre/"

archivo_entrada= path + "tp3/src/experimentacion/ejercicio1/exp2/casos.in"
#--constantes
cant_repeticiones = 8


#--VALORES EN LA SALIDA DEL PROGRAMA:
#-- cantidad gimnasios
#-- cantidad paradas
#-- capacidad mochila
#-- repeticion
#-- tiempo total
#-- cantidad de instancias que visito
#-- cantidad de instancias que calculo
#-- tamano del camino solucion
#-- version de algoritmo (podas)
#-- cantidad de podas 1
#-- cantidad de podas 2

#sys.stdout.write("\n")
#sys.stdout.write("\n")
#sys.stdout.write("----------------------------------------------------------\n")
#sys.stdout.write("------------------------ VERSION 0 -----------------------\n")
#sys.stdout.flush()
#
#entrada = csv.reader(open(archivo_entrada, "rb"))
#
#archivo_salida = path + "tp3/src/experimentacion/ejercicio1/exp2/version0.csv"
#salida = csv.writer(open('%s' % str(archivo_salida), "a"))
#
#salida.writerow(["Cantidad de gimnasios", "Cantidad de paradas", "Capacidad de la mochila", "Numero de repeticion", "Tiempo", "Cantidad de instancias visitadas", "Cantidad de instancias calculadas", "Tamano del camino", "Version de podas", "Cantidad de podas 1", "Cantidad de podas 2"])
#
#datos_entrada = ""
#for fila in entrada:
#
#	if len(fila) > 0:
#	
#		datos_entrada += " "+fila[0]
#	
#	elif len(datos_entrada) > 0:
#
#		for j in xrange(0, cant_repeticiones):
#
#			status, corrida = commands.getstatusoutput("echo '"+datos_entrada+"' | "+path+"tp3/src/soluciones/ejercicio1_0")
#			valores = np.fromstring(corrida, sep=',')
#			if len(valores) >= 10:
#				salida.writerow([valores[0], valores[1], valores[2], int(j), valores[3], valores[4], valores[5], valores[6], valores[7], valores[8], valores[9]])
#				print "-- gimnasios: "+str(valores[0])+" -- paradas: "+str(valores[1])+" -- mochila: "+str(valores[2])+" -- "+str(j)+"/"+str(cant_repeticiones)
#		
#		datos_entrada = ""




for version in xrange(1,5):

	sys.stdout.write("\n")
	sys.stdout.write("\n")
	sys.stdout.write("----------------------------------------------------------\n")
	sys.stdout.write("------------------------ VERSION "+str(version)+" -----------------------\n")
	sys.stdout.flush()

	entrada = csv.reader(open(archivo_entrada, "rb"))

	archivo_salida = path + "tp3/src/experimentacion/ejercicio1/exp2/version"+str(version)+".csv"

	num = 1
	header_dat = ""
	datos_entrada = ""
	for fila in entrada:

		if len(fila) > 0:
			if header_dat == "":
				header_dat = fila[0]
			datos_entrada += " "+fila[0]
		
		elif len(datos_entrada) > 0:

			for j in xrange(0, cant_repeticiones):
				
				sys.stdout.write("corrida: "+str(num)+" - datos: "+str(header_dat)+" - rep: "+str(j)+"/"+str(cant_repeticiones)+"\n")
				sys.stdout.flush()

				status, corrida = commands.getstatusoutput("echo '"+datos_entrada+" "+str(version)+" "+str(j)+"' | "+path+"tp3/src/soluciones/ejercicio1"+" >> "+archivo_salida)

				num += 1

			datos_entrada = ""
			header_dat = ""
