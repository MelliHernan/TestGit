#!/usr/bin/env python

import socket
import sys
from datetime import datetime
import errno

remoteServer    = input("Ingrese el host remoto para escanear: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

print("Ingrese el rango de puertos que le gustaria escanear en el equipo: ")
startPort    = input("Ingrese un puerto de inicio: ")
endPort    = input("Enter un puerto final: ")

print("Espere por favor, escaneando el host remoto...", remoteServerIP)

time_init = datetime.now()

try:
	for port in range(int(startPort),int(endPort)):
		print ("Comprobando puerto {} ...".format(port))
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(5)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			print("Puerto {}: 	 Abierto".format(port))
		else:
			print("Puerto {}: 	 Cerrado".format(port))
			print("Razon:",errno.errorcode[result])
		sock.close()

except KeyboardInterrupt:
	print("Presionaste Ctrl+C")
	sys.exit()
except socket.gaierror:
	print('No se puede resolver el nombre de host. Exiting')
	sys.exit()
except socket.error:
	print("No se puede conectar al servidor")
	sys.exit()

time_finish = datetime.now()
total =  time_finish - time_init
print('Escaneo de puertos completado en: ', total)
