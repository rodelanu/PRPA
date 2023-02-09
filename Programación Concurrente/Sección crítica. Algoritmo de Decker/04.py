
"""

Este programa ilustra el uso de un algoritmo de sección crítica basado en el 
algoritmo de Peterson. La sección crítica es una parte del código que solo debe 
ser ejecutada por un proceso o hilo a la vez, para evitar conflictos o problemas 
de consistencia.

El programa crea una lista de procesos lp y una variable compartida common para 
mantener un contador. También hay una matriz compartida critical y una variable 
compartida turn para implementar el algoritmo de Peterson.

La función task representa un proceso que se ejecuta en paralelo y la función 
is_anybody_inside se utiliza para verificar si algún otro proceso está en su 
sección crítica. La función task realiza un bucle for 100 veces, que incluye una 
sección no crítica, una sección crítica y una sección final no crítica. 
En la sección no crítica, simplemente se aumenta una variable local a.

En la sección crítica, el proceso actual marca su entrada en la sección crítica 
en la matriz compartida critical, y luego verifica si algún otro proceso está en 
su sección crítica con la función is_anybody_inside. Si algún otro proceso está 
en su sección crítica, el proceso actual da su turno y vuelve a intentar acceder 
a la sección crítica. De lo contrario, el proceso actual incrementa el contador 
compartido common y marca su salida de la sección crítica en la matriz critical.

La función main crea los procesos, imprime el valor inicial del contador, ejecuta 
los procesos y espera a que terminen antes de imprimir el valor final del contador y "fin".

El algoritmo de Peterson permite garantizar que solo un proceso acceda a la sección 
crítica a la vez, asegurando la consistencia de los datos compartidos.

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

def task(common, tid, critical, turn):
   a = 0
   for i in range(100):
      print (f'{tid}-{i}: Non-critical Section')
      a += 1
      print (f'{tid}-{i}: End of non-critical Section')
      critical[tid] = 1
      while is_anybody_inside(critical, tid):
         critical[tid] = 0
         print (f'{tid}-{i}: Giving up')
         while turn.value==tid:
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
   turn = Value('i', 0)
   for tid in range(N):
      lp.append(Process(target=task, args=(common, tid, critical, turn)))
   print (f"Valor inicial del contador {common.value}")
   for p in lp:
      p.start()

   for p in lp:
      p.join()

   print (f"Valor final del contador {common.value}")
   print ("fin")

if __name__ == "__main__":
   main()