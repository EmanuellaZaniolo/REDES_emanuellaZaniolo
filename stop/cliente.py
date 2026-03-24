import socket

HOST = "127.0.0.1"
PORT = 9002

mensagem = input("[Cliente] Mensagem: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((HOST, PORT))
    letra = cliente.recv(1024).decode()
    print("Letra sorteada: ",letra)
    mensagem = cliente.recv(1024).decode()
    resposta = input (mensagem.decode())
    cliente.sendall(resposta.encode())

    