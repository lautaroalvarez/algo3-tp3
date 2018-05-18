import numpy as np
import csv, commands, sys

path = "/home/matias/algo3segundocuatrimestre/"

archivo_entrada = path + "tp3/src/experimentacion/ejercicio2/exp2/casos.in"
#--constantes
cant_repeticiones = 20

sys.stdout.write("\n")
sys.stdout.write("\n")
sys.stdout.write("-------------------------------------------------------------\n")
sys.stdout.write("---------------- CORRIDA AUMENTANDO GIMNASIOS ---------------\n")
sys.stdout.flush()

entrada = csv.reader(open(archivo_entrada, "rb"))

archivo_salida = path + "tp3/src/experimentacion/ejercicio2/exp2/corrida.csv"

commands.getstatusoutput("echo 'Codigo de caso, Cantidad de gimnasios, Cantidad de paradas, Capacidad de la mochila, Tiempo, Distancia del camino, Cantidad de cambios, Codigo de vecindad' >> "+archivo_salida)

vecindades = np.array(['0001','0011','0111','1111'])

header_dat = ""
datos_entrada = ""
for fila in entrada:

	if len(fila) > 0:
		if header_dat == "":
			header_dat = fila[0]
		datos_entrada += " "+fila[0]
	
	elif len(datos_entrada) > 0:

		#--corre para ej3
		for vecindad in vecindades:
	
			for j in xrange(0, cant_repeticiones):
			
				sys.stdout.write("ej4 - datos: "+str(header_dat)+" - codigo: "+vecindad+" - rep: "+str(j)+"/"+str(cant_repeticiones)+"\n")
				sys.stdout.flush()

				status, corrida = commands.getstatusoutput("echo '"+datos_entrada+" "+vecindad+"' | "+path+"tp3/src/soluciones/ejercicio2 >> "+archivo_salida)
		
		
		#--corre para ej1
#		for j in xrange(0, cant_repeticiones):
#			sys.stdout.write("ej1 - datos: "+str(header_dat)+" - codigo: "+str(codigo)+" - rep: "+str(j)+"/"+str(cant_repeticiones)+"\n")
#			sys.stdout.flush()
#			status, corrida = commands.getstatusoutput("echo '"+datos_entrada+"' | "+path+"tp3/src/soluciones/ejercicio1 >> "+archivo_salida)

		datos_entrada = ""
		header_dat = ""
