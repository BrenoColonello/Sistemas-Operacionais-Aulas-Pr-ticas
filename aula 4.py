import threading
import time
import random

# Número de filósofos
NUM_FILOSOFOS = 5

# Semáforo para cada garfo
garfos = [threading.Semaphore(1) for _ in range(NUM_FILOSOFOS)]

# Função para o comportamento de cada filósofo
def filosofo(id):
    while True:
        # O filósofo está pensando
        print(f"Filósofo {id} está pensando.")
        time.sleep(random.uniform(1, 3))  # Simula o tempo de pensar

        # O filósofo tenta pegar os garfos
        print(f"Filósofo {id} está com fome.")
        
        # Para evitar deadlock, o filósofo pega primeiro o garfo de menor índice
        if id % 2 == 0:  # Filósofos pares pegam o garfo esquerdo primeiro
            garfos[id].acquire()
            garfos[(id + 1) % NUM_FILOSOFOS].acquire()
        else:  # Filósofos ímpares pegam o garfo direito primeiro
            garfos[(id + 1) % NUM_FILOSOFOS].acquire()
            garfos[id].acquire()

        # O filósofo está comendo
        print(f"Filósofo {id} está comendo.")
        time.sleep(random.uniform(1, 2))  # Simula o tempo de comer

        # O filósofo devolve os garfos
        garfos[id].release()
        garfos[(id + 1) % NUM_FILOSOFOS].release()

        print(f"Filósofo {id} terminou de comer e devolveu os garfos.")

# Criar threads para cada filósofo
filosofos = []
for i in range(NUM_FILOSOFOS):
    t = threading.Thread(target=filosofo, args=(i,))
    filosofos.append(t)
    t.start()

# Manter o programa rodando
for t in filosofos:
    t.join()