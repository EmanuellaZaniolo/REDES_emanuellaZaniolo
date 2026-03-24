import socket
HOST = "0.0.0.0" #String
PORT = 2227 #int

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
   s.bind((HOST, PORT)) # solicita "nesse endereço e nessa porta você reserva pra mim"
   s.listen(1)# está esperando chegar

   # Aguarda jogadores entrarem
   print("[Server] Aguardando jogador 1".encode())
   conn_1, addr_1 = s.accept()
   conn_1.sendall("[Server] OK. você é o jogador 1".encode())
   conn_1.sendall("[Server] Aguardando jogador 2 entrar".encode())

   conn_2, addr_2 = s.accept()
   conn_2.sendall("[Server] OK. você é o jogador 2".encode())
   conn_2.sendall("[Server] Aguardando o jogador 1 jogar".encode())

   print("ambos entraram")
   while cj1 < 3 or cj2 < 3:
       print("[Server] Aguardando a jogada do 1")   
       conn_1.sendall("[Server] Faça a sua jogada".encode())
       j1 = conn_1.recv(1024).decode()

       print("[Server] Aguardando a jogada do 2")   
       conn_2.sendall("[Server] Faça a sua jogada".encode())
       j2 = conn_2.recv(1024).decode()
       cj1 = 0
       cj2 = 0

       if j1 == j2:
           msg = "Empate"

       match j1:
           case "pedra":
               if j2 == "papel":
                   msg = "Jogador 2 ganhou"
                   cj2 = cj2+1
               if j2 == "tesoura":
                   msg = "Jogador 1 ganhou"
                   cj1 = cj1+1
           case "papel":
               if j2 == "pedra":
                   msg = "Jogador 1 ganhou"
                   cj1 = cj1+1
               if j2 == "tesoura":
                   msg = "Jogador 2 ganhou"
                   cj2 = cj2+1
           case "tesoura":
               if j2 == "papel":
                   msg = "Jogador 1 ganhou"
                   cj1 = cj1+1
               if j2 == "pedra":
                   msg = "Jogador 2 ganhou"
                   cj2 = cj2+1

       conn_1.sendall(msg.encode())
       conn_2.sendall(msg.encode())

       print(msg)
  
   if cj2 > cj1:
       print("jogador 2 ganhou todas")
   if cj1 > cj2:
       print("jogador 2 ganhou todas")

   conn_1.close()
   conn_2.close()
