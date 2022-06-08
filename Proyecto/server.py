import socket


HOST = "localhost" #Ip del cliente, esta ip es el LocalHost(propio equipo)
PORT = 65123 #Este es el puerto de escucha

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:#Se abre el socket para escuchar a las entradas
                                                            #Se especifica el detalle de IP y el de protocolo, AF_INET es Ipv4, SOCK_STREAM es el protocolo TCP
    s.bind((HOST, PORT)) #Se asocia el socket, se especifica el HOST y el PUERTO
    s.listen() #Se pone el socket en modo escucha
    conn, addr = s.accept() #Se acepta conexiones entrantes, retorna el socket de entrada y la direccion

    with conn:
        print(f"Conectando a {addr}: ") #Se muestra un mensaje para saber a donde se esta conectando
        while True: #Recibira los datos
            data = conn.recv(1024) #Se especifica el tamaño de datos que se recibira, 1024 es un k de datos
            if not data: #Si no llega nada, se termina
                break

            conn.sendall(data) #Se retorna lo que se envio