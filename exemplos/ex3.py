import threading
import time

WAITING_TIME = 0.1

# Semáforo
semaforo = threading.Semaphore(0)
# contador

def thread_0():
    for i in range(1, 11):
        semaforo.acquire() #fica parado se o valor permanecer o mesmo, se ele aumentar passa tbm
    
        print(f"[Thread 0] {i}", flush=True)
    
        semaforo.release()
        #oq ta entre o aquire e o realese so um cliente entra
        time.sleep(WAITING_TIME)

#quando alguem incrementa e um acquire comeca não tem como saber qual thread vai entrar, o SO que decide 
def thread_1():
    for i in range(1, 11):
        semaforo.acquire()
        
        print(f"[Thread 1] {i}", flush=True)
    
        semaforo.release()
        time.sleep(WAITING_TIME)


# Instancia as threads
t0 = threading.Thread(target=thread_0)
t1 = threading.Thread(target=thread_1)

# Starta as threads
t0.start()
t1.start()

# Libera o semáforo
semaforo.release()

# Aguarda as threads finalizarem
print("[Main] Aguardando threads")
t0.join()
t1.join()

print("[Main] Finalizado")