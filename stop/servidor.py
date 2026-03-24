import socket
import threading
from time import sleep

HOST = "0.0.0.0"
PORT = 9002
semaforo = threading.Semaphore(0)
LETRA = ""
CEP = ["",""]
NOME = ["",""]

WAITING_TIME = 3

def atender_cliente(conn, addr, tid):
    global CEP
    global NOME

    semaforo.acquire()
    with conn:
        conn.sendall(LETRA.encode())
        conn.sendall("CEP: ".encode)
        resposta = conn.recv(1024).decode("")
        print(f"Cliente {tid} responde: {resposta}")
    pass

def iniciar_servidor():
    global LETRA
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)#deixar usar a msm porta 2x
        server.bind((HOST, PORT))
        server.listen()

        print(f"Servidor ouvindo em {HOST}:{PORT}")

        #aguarda jogador1
        conn_1, addr_1 = server.accept() #para ate q o cliente conecta
        thread_1 = threading.Thread(target=atender_cliente,args=(conn_1,addr_1,0),deamon=True)
        #em thread atender cliente é um parametro entaão passa paremetro em linha diferente(45)
        thread_1.start()

        #aguarda jogador2
        conn_2, addr_2 = server.accept() #para ate q o cliente conecta
        thread_2 = threading.Thread(target=atender_cliente,args=(conn_2,addr_2,1),deamon=True)
        #em thread atender cliente é um parametro entaão passa paremetro em linha diferente(45)
        thread_2.start()

        LETRA="T"

        semaforo.release()
        semaforo.release()

        thread_1.join()
        thread_2.join()




if __name__ == "__main__":
    iniciar_servidor()