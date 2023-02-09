
"""

Este programa es un ejemplo de implementación del algoritmo de Dekker en Python 
utilizando el módulo "multiprocessing".

El objetivo del algoritmo es garantizar la exclusión mutua, es decir, que solo 
un proceso pueda ejecutar una sección crítica (donde se accede a un recurso
compartido) a la vez.

El programa crea varios procesos (cantidad determinada por la variable N) que 
llaman a la función "task". Cada proceso tiene su identificador (tid) y accede 
a un contador compartido (common) y a una variable de turno (turn).

En cada iteración, el proceso imprime su identificador y un mensaje indicando 
que está en la sección no crítica, luego realiza una operación simple (incrementa 
una variable local "a") y vuelve a imprimir un mensaje indicando el fin de la 
sección no crítica.

Luego, el proceso entra en un bucle que verifica si es su turno de acceder a la 
sección crítica. Si no es su turno, el proceso espera. Cuando es su turno, el 
proceso imprime un mensaje indicando que está en la sección crítica y realiza 
una operación simple en el contador compartido (incrementándolo en 1). 
Finalmente, imprime un mensaje indicando el fin de la sección crítica y actualiza 
la variable de turno para que sea el turno del siguiente proceso.

El programa principal crea los procesos y los inicia, luego los espera a todos 
para terminar. Al final, imprime el valor inicial y final del contador compartido y
un mensaje de fin.

Es importante destacar que este programa solo es una implementación de ejemplo y 
puede no ser la más eficiente o segura para un entorno real, y que el uso de 
exclusión mutua puede requerir consideraciones adicionales como la detección de 
deadlocks y la prevención de interbloqueos.

"""

from multiprocessing import Process, Value

N = 8
def task(common, tid, turn):
   a = 0
   for i in range(100):
      print (f'{tid}-{i}: Non-critical Section')
      a += 1
      print (f'{tid}-{i}: End of non-critical Section')
      while turn.value!=tid:
         pass
      print (f'{tid}-{i}: Critical section')
      v = common.value + 1
      print (f'{tid}-{i}: Inside critical section')
      common.value = v
      print (f'{tid}-{i}: End of critical section')
      turn.value = (tid + 1) % N

def main():
   lp = []
   common = Value('i', 0)
   turn = Value('i', 0)
   for tid in range(N):
      lp.append(Process(target=task, args=(common, tid, turn)))
   print (f"Valor inicial del contador {common.value}")
   for p in lp:
      p.start()
  
   for p in lp:
      p.join()

   print (f"Valor final del contador {common.value}")
   print ("fin")

if __name__ == "__main__":
   main()