import threading
import time

#lock que sera usado incorretamente
lock = threading.Lock()

#lista para registrar a ordem de execução
registro_execucao = []

def tarefa_com_bug(nome):
    lock.acquire()
    registro_execucao.append(f"{nome} entrou na seção crítica")
    time.sleep(1)  # Simula o tempo de execução da tarefa
    if nome == "Tarefa 1":
        registro_execucao.append(f"{nome} terminou mas Nao Liberou lock") #simula erro esquecimento
        return # esquece de liberar o lock
    else:
        registro_execucao.append(f"{nome} terminou e liberou o lock")
        lock.release()

# criar duas threads
t1 = threading.Thread(target=tarefa_com_bug, args=("Tarefa 1",))
t2 = threading.Thread(target=tarefa_com_bug, args=("Tarefa 2",))

# iniciar as threads
t1.start()
time.sleep(0.2)  # Garante que a Tarefa 1 comece primeiro
t2.start()

#espera ambas( t2 pode travar)
t1.join(timweout=3) 
t2.join(timeout=3)

registro_execucao.append("Tarefa 1 e Tarefa 2 terminaram")

registro_execucao