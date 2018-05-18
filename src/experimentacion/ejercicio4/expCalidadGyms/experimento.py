import numpy as np
import csv, commands, sys

path = "/home/john/Desktop/Algo3/algo3segundocuatrimestre/"

archivo_entrada = path + "tp3/src/experimentacion/ejercicio4/expCalidadGyms/casos.in"
#--constantes
cant_repeticiones = 1

sys.stdout.write("\n")
sys.stdout.write("\n")
sys.stdout.write("-------------------------------------------------------------\n")
sys.stdout.write("----------------- CORRIDA AUMENTANDO PARADAS ----------------\n")
sys.stdout.flush()

entrada = csv.reader(open(archivo_entrada, "rb"))

archivo_salida = path + "tp3/src/experimentacion/ejercicio4/expCalidadGyms/corrida.csv"

commands.getstatusoutput("echo 'Cantidad de gimnasios, Cantidad de pokeparadas, Capacidad mochila, Diferencia' >> "+archivo_salida)

vecindad = '1111'

header_dat = ""
datos_entrada = ""
for fila in entrada:

	if len(fila) > 0:
		if header_dat == "":
			header_dat = fila[0]
		datos_entrada += " "+fila[0]
	
	elif len(datos_entrada) > 0:

		#--corre para ej3
		for j in xrange(0, cant_repeticiones):
		
			sys.stdout.write("ej4 - datos: "+str(header_dat)+" - codigo: "+vecindad+" - rep: "+str(j)+"/"+str(cant_repeticiones)+"\n")
			sys.stdout.flush()
			status1, corrida1 = commands.getstatusoutput("echo '"+datos_entrada+"' | "+path+"tp3/src/soluciones/ejercicio4")

			status2, corrida2 = commands.getstatusoutput("echo '"+datos_entrada+"' | "+path+"tp3/src/soluciones/ejercicio1")
			print corrida1
			print corrida2
			#print float(corrida2) - float(corrida1)
		#--corre para ej1
#		for j in xrange(0, cant_repeticiones):
#			sys.stdout.write("ej1 - datos: "+str(header_dat)+" - codigo: "+str(codigo)+" - rep: "+str(j)+"/"+str(cant_repeticiones)+"\n")
#			sys.stdout.flush()
#			status, corrida = commands.getstatusoutput("echo '"+datos_entrada+"' | "+path+"tp3/src/soluciones/ejercicio1 >> "+archivo_salida)

		datos_entrada = ""
		header_dat = ""
