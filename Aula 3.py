import threading
import time
import matplotlib.pyplot as plt

# Número máximo de threads que podem acessar simultaneamente
MAX_RECURSOS = 3

# Semáforo permitindo até MAX_RECURSOS threads
semaforo = threading.Semaphore(MAX_RECURSOS)

# Lock tradicional (exclusão total)
lock = threading.Lock()

# Registros para visualização
acessos_com_semaforo = []
acessos_com_lock = []

# Função simulando acesso a um recurso limitado
def acessar_recurso_com_semaforo(thread_id):
    for _ in range(3):
        #semaforo.acquire()
        with semaforo:
          acessos_com_semaforo.append((thread_id, time.time()))
          time.sleep(0.5)  # Simula tempo de uso do recurso
        #semaforo.release()

# Função simulando acesso ao mesmo recurso com lock (exclusivo)
def acessar_recurso_com_lock(thread_id):
    for _ in range(3):
        #lock.acquire()
        with lock:
          acessos_com_lock.append((thread_id, time.time()))
          time.sleep(0.5)
        #lock.release()

# Criar e executar threads para ambos os casos
def simular_acessos():
    threads_semaforo = [threading.Thread(target=acessar_recurso_com_semaforo, args=(i,)) for i in range(6)]
    threads_lock = [threading.Thread(target=acessar_recurso_com_lock, args=(i,)) for i in range(6)]

    # Iniciar com semáforo
    for t in threads_semaforo:
        t.start()
    for t in threads_semaforo:
        t.join()

    # Iniciar com lock
    for t in threads_lock:
        t.start()
    for t in threads_lock:
        t.join()

# Executar simulação
simular_acessos()

# Preparar dados para o gráfico
tempos_s, ids_s = zip(*acessos_com_semaforo)
tempos_l, ids_l = zip(*acessos_com_lock)

# Plotar
plt.figure(figsize=(14, 6))

# Semáforo
plt.subplot(1, 2, 1)
plt.scatter(tempos_s, ids_s, c='blue')
plt.title("Acessos com Semáforo (3 simultâneos)")
plt.xlabel("Tempo")
plt.ylabel("ID da Thread")
plt.grid(True)

# Lock
plt.subplot(1, 2, 2)
plt.scatter(tempos_l, ids_l, c='red')
plt.title("Acessos com Lock (1 por vez)")
plt.xlabel("Tempo")
plt.ylabel("ID da Thread")
plt.grid(True)

plt.tight_layout()
plt.show()

