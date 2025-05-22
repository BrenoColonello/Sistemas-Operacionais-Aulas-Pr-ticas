import threading  # Importa a biblioteca para trabalhar com threads
import time       # Para adicionar pausas (sleep)
import random     # Para gerar tempos aleatórios

N = 5  # Número de filósofos (e garfos)

# Cria uma lista de semáforos, um para cada garfo
semaforos = [threading.Semaphore(1) for _ in range(N)]

# Função que representa o comportamento de cada filósofo
def filosofo(i):
    while True:
        print(f"Filósofo {i} está pensando...")  # Estado: pensando
        time.sleep(random.uniform(0.5, 1.5))    # Espera um tempo aleatório
        print(f"Filósofo {i} está com fome.")   # Estado: com fome
        semaforos[i].acquire()                 # Pega o garfo à esquerda
        semaforos[(i + 1) % N].acquire()       # Pega o garfo à direita (com wrap-around)
        print(f"Filósofo {i} está comendo.")    # Estado: comendo
        time.sleep(random.uniform(0.5, 1.5))    # Come por um tempo aleatório
        print(f"Filósofo {i} terminou de comer.")  # Termina de comer
        semaforos[i].release()                 # Solta o garfo à esquerda
        semaforos[(i + 1) % N].release()       # Solta o garfo à direita

# Cria e inicia uma thread para cada filósofo
for i in range(N):
    threading.Thread(target=filosofo, args=(i,), daemon=True).start()

time.sleep(10)  # Executa o programa por 10 segundos antes de encerrar
