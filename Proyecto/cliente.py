import socket

HOST = "127.0.0.1" #Ip del servidor, esta ip es el LocalHost(propio equipo)
PORT = 65123 #Este es el puerto de envio

with socket.socket(socket.AF_INET, socket.SOCK_STREAM)as s: #Se especifica el detalle de IP y el de protocolo, AF_INET es Ipv4, SOCK_STREAM es el protocolo TCP
    s.connect((HOST, PORT)) #Se conectara a un HOST y a un PUERTO

    s.sendall(b"Hola Mundo") #Se envia datos

    data = s.recv(1024) #Se especifica el tamaño de datos que se recibira, 1024 es un k de datos

print("Recibido,", repr(data)) #Mostrara un mensaje que nos dira que recibio los datos