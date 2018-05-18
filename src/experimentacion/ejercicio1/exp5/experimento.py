import numpy as np
import csv, commands, sys

path = "/home/laucha/Documentos/algo3segundocuatrimestre/"

archivo_entrada = path + "tp3/src/experimentacion/ejercicio1/exp5/casos.in"
#--constantes
cant_repeticiones = 5

sys.stdout.write("\n")
sys.stdout.write("\n")
sys.stdout.write("-------------------------------------------------------------\n")
sys.stdout.write("------------------------ CORRIDA LOCA -----------------------\n")
sys.stdout.flush()

entrada = csv.reader(open(archivo_entrada, "rb"))

archivo_salida = path + "tp3/src/experimentacion/ejercicio1/exp5/corrida.csv"

commands.getstatusoutput("echo 'Cantidad de gimnasios,Cantidad de paradas,Capacidad de la mochila,Numero de repeticion,Tiempo,Cantidad de instancias visitadas,Cantidad de instancias calculadas,Tamano del camino,Version de podas,Cantidad de podas 1,Cantidad de podas 2,Pociones Gimnasio' >> "+archivo_salida)

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

			status, corrida = commands.getstatusoutput("echo '"+datos_entrada+" 4 "+str(j)+"' | "+path+"tp3/src/soluciones/ejercicio1 >> "+archivo_salida)
		
		num += 1
		datos_entrada = ""
		header_dat = ""
