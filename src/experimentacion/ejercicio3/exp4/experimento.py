import numpy as np
import csv, commands, sys

path = "/home/laucha/Documentos/algo3segundocuatrimestre/"

archivo_entrada = path + "tp3/src/experimentacion/ejercicio3/exp2/casos.in"
#--constantes
cant_repeticiones = 5

sys.stdout.write("\n")
sys.stdout.write("\n")
sys.stdout.write("-------------------------------------------------------------\n")
sys.stdout.write("------------------------ CORRIDA LOCA -----------------------\n")
sys.stdout.flush()

entrada = csv.reader(open(archivo_entrada, "rb"))

archivo_salida = path + "tp3/src/experimentacion/ejercicio3/exp2/corrida.csv"

#commands.getstatusoutput("echo 'Codigo de caso, Cantidad de gimnasios, Cantidad de paradas, Capacidad de la mochila, Tiempo, Distancia del camino, Cantidad de cambios, Codigo de vecindad' >> "+archivo_salida)

header_dat = ""
datos_entrada = ""
for fila in entrada:

	if len(fila) > 0:
		if header_dat == "":
			header_dat = fila[0]
		datos_entrada += " "+fila[0]
	
	elif len(datos_entrada) > 0:

#		for c1 in xrange(0, 2):
#			for c2 in xrange(0, 2):
#				for c3 in xrange(0, 2):
#					for c4 in xrange(0, 2):
#	
#						codigo = str(c1)+str(c2)+str(c3)+str(c4)
#						
#						for j in xrange(0, cant_repeticiones):
#						
#							sys.stdout.write("datos: "+str(header_dat)+" - rep: "+str(j)+"/"+str(cant_repeticiones)+"\n")
#							sys.stdout.flush()
#
#							status, corrida = commands.getstatusoutput("echo '"+datos_entrada+" "+codigo+"' | "+path+"tp3/src/soluciones/ejercicio3 >> "+archivo_salida)

		for j in xrange(0, cant_repeticiones):
		
			sys.stdout.write("datos: "+str(header_dat)+" - rep: "+str(j)+"/"+str(cant_repeticiones)+"\n")
			sys.stdout.flush()
			status, corrida = commands.getstatusoutput("echo '"+datos_entrada+"' | "+path+"tp3/src/soluciones/ejercicio1 >> "+archivo_salida)
	
		
		datos_entrada = ""
		header_dat = ""
