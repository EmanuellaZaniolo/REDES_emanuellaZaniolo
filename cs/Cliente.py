# Cliente
import socket

HOST = "127.0.0.1"
PORT = 2227

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   # Conecta com o servidor
   s.connect((HOST, PORT))

   # Recebe mensagem do servidor
   msg = s.recv(1024).decode()
   print(msg)
   msg = s.recv(1024).decode()
   print(msg)

   while True:
       msg = s.recv(1024).decode()
       print(msg)
       resposta = input("Resposta: ")
       s.sendall(resposta.encode())

       msg = s.recv(1024).decode()
       print(msg)