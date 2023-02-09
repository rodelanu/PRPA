
"""

Este código crea un conjunto de procesos en paralelo que ejecutan la función "f".
La función "f" recibe un valor "value" y, en tres iteraciones, imprime "hola soy" 
seguido de "value" y "vuelta" seguido del número de la iteración. Antes de cada 
impresión, la función "sleep" detiene la ejecución del programa por un número de 
segundos generado por la función "random.random()/3".

El código también contiene la función "g" que solo imprime "adios".

La línea "if name == "main":" asegura que el código dentro de ella solo se ejecute 
cuando se ejecute el archivo directamente y no cuando se importe como módulo.

El código crea una lista "lp" de objetos de proceso, donde cada proceso ejecuta 
la función "f" con un argumento diferente, "ana0", "ana1", ..., "ana9". 
Luego, se inician todos los procesos en la lista "lp" llamando a sus métodos "start".

Además, se crea un proceso "q" que ejecuta la función "g" y se inicia. 
Finalmente, se imprime "fin".

Es importante notar que, debido a que los procesos son ejecutados en paralelo, 
el orden en que aparecen las impresiones "hola soy" y "adios" no está garantizado y 
puede variar en cada ejecución.

"""


import time
import random

from multiprocessing import Process

def f(value):
   for i in range(3):
      print (f"hola soy {value} vuelta {i}")
      time.sleep(random.random()/3)

def g():
   print ("adios")

if __name__ == "__main__":
   N = 10
   lp = []
   for i in range(N):
      lp.append(Process(target=f,args=(f"ana{i}",)))
   for p in lp:
      p.start()

   q = Process(target=g)
   q.start()
   print ("fin")