import numpy as np
import csv, commands, sys

path = "/home/laucha/Documentos/algo3segundocuatrimestre/"

archivo_entrada = path + "tp3/src/experimentacion/ejercicio3/ejemplo_cambios/caso.in"

sys.stdout.write("\n")
sys.stdout.write("\n")
sys.stdout.write("-----------------------------------------------------\n")
sys.stdout.write("----------------- CORRIDA DE UN CASO ----------------\n")
sys.stdout.flush()

entrada = csv.reader(open(archivo_entrada, "rb"))

archivo_salida = path + "tp3/src/experimentacion/ejercicio3/ejemplo_cambios/corrida.csv"

commands.getstatusoutput("echo 'Cantidad de cambios,Distancia del camino,Mejora,Tamano de vecindad,Codigo de vecindad' >> "+archivo_salida)

vecindad = '1111'

header_dat = ""
datos_entrada = ""
for fila in entrada:

	if len(fila) > 0:
		if header_dat == "":
			header_dat = fila[0]
		datos_entrada += " "+fila[0]


status, corrida = commands.getstatusoutput("echo '"+datos_entrada+" "+vecindad+"' | "+path+"tp3/src/soluciones/ejercicio3 >> "+archivo_salida)