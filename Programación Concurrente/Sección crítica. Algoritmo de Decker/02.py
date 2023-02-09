
"""

Este programa es otro ejemplo de solución al problema de sección crítica usando 
el algoritmo de Dekker. La sección crítica se implementa de forma similar a la 
primera solución, pero en lugar de utilizar una variable "turn", se utiliza un 
arreglo "critical" de N elementos, cada uno de los cuales representa un proceso. 
Cada proceso marca su posición en el arreglo "critical" como 1 al entrar a la 
sección crítica y la vuelve a 0 al salir.

El proceso espera a que todos los demás procesos estén fuera de la sección crítica 
antes de entrar a ella, chequeando si hay algún proceso en la sección crítica con 
la función "is_anybody_inside". Si algún otro proceso está en la sección crítica, 
el proceso espera.

La solución garantiza la exclusión mutua, es decir, que solo un proceso a la vez 
puede entrar a la sección crítica. Al final del programa, se imprime el valor final 
del contador común, que debería ser 800 si todos los procesos ejecutaron correctamente.

"""

from multiprocessing import Process, Value, Array

N = 8

def is_anybody_inside(critical, tid):
   found = False
   i = 0
   while i<len(critical) and not found:
      found = tid!=i and critical[i]==1
      i += 1
   return found

def task(common, tid, critical):
   a = 0
   for i in range(100):
      print (f'{tid}-{i}: Non-critical Section')
      a += 1
      print (f'{tid}-{i}: End of non-critical Section')
      while is_anybody_inside(critical, tid):
         pass
      critical[tid] = 1
      print (f'{tid}-{i}: Critical section')
      v = common.value + 1
      print (f'{tid}-{i}: Inside critical section')
      common.value = v
      print (f'{tid}-{i}: End of critical section')
      critical[tid] = 0

def main():
   lp = []
   common = Value('i', 0)
   critical = Array('i', [0]*N)
   for tid in range(N):
      lp.append(Process(target=task, args=(common, tid, critical)))
   print (f"Valor inicial del contador {common.value}")
   for p in lp:
      p.start()

   for p in lp:
      p.join()

   print (f"Valor final del contador {common.value}")
   print ("fin")

if __name__ == "__main__":
   main()