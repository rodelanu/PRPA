
"""

Este código crea dos procesos en paralelo que ejecutan la función "f". 
La función "f" imprime "hola" y un número (de 0 a 4) en cinco iteraciones. 
Antes de cada impresión, la función "sleep" detiene la ejecución del programa 
por un número de segundos aleatorios, generado por la función "random".

La línea "if __name__ == "__main__":" asegura que el código dentro de ella solo se 
ejecute cuando se ejecute el archivo directamente y no cuando se importe como módulo.

El código crea dos objetos de proceso, "p" y "q", utilizando la clase "Process" y 
estableciendo la función "f" como la función de destino a ejecutar. A continuación, 
se inician ambos procesos llamando a sus métodos "start". Finalmente, se imprime "fin".

Es importante notar que, debido a que los procesos son ejecutados en paralelo, 
el orden en que aparecen las impresiones "hola" no está garantizado y 
puede variar en cada ejecución.

"""


from time import sleep
from random import random

from multiprocessing import Process

def f():
   for i in range(5):
      print ("hola", i)
      sleep(random())

if __name__ == "__main__":
   p = Process(target=f)
   q = Process(target=f)
   p.start()
   q.start()
   print ("fin")