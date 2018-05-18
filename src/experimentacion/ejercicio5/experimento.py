import numpy as np
import csv, commands, sys

path = "/home/laucha/Documentos/algo3segundocuatrimestre/"

archivo_entrada = path + "tp3/src/experimentacion/ejercicio5/casos.in"
#--constantes
cant_repeticiones = 5

sys.stdout.write("\n")
sys.stdout.write("\n")
sys.stdout.write("-------------------------------------------------------------\n")
sys.stdout.write("------------------------ CORRIDA LOCA -----------------------\n")
sys.stdout.flush()

entrada = csv.reader(open(archivo_entrada, "rb"))

archivo_salida = path + "tp3/src/experimentacion/ejercicio5/corrida.csv"

commands.getstatusoutput("echo 'Codigo de caso, Cantidad de gimnasios, Cantidad de paradas, Capacidad de la mochila, Tiempo, Distancia del camino, Ejercicio' >> "+archivo_salida)

num = 1
header_dat = ""
datos_entrada = ""
for fila in entrada:

	if len(fila) > 0:
		if header_dat == "":
			header_dat = fila[0]
		datos_entrada += " "+fila[0]
	
	elif len(datos_entrada) > 0:

		for i in xrange(1, 5):
			
			ejecutable = "ejercicio"+str(i)

			for j in xrange(0, cant_repeticiones):
			
				sys.stdout.write("corrida: "+str(num)+" - datos: "+str(header_dat)+" - programa: "+str(i)+" - rep: "+str(j)+"/"+str(cant_repeticiones)+"\n")
				sys.stdout.flush()

				status, corrida = commands.getstatusoutput("echo '"+datos_entrada+"' | "+path+"tp3/src/soluciones/"+ejecutable+" >> "+archivo_salida)
			
			num += 1
		datos_entrada = ""
		header_dat = ""
