
"""

Este código es similar al código anterior, pero con algunas diferencias importantes.

En este código, la función "f" hace uso de la función "current_process()" de la 
biblioteca "multiprocessing" para obtener información sobre el proceso actual en 
cada iteración. La función "current_process()" devuelve un objeto de proceso que 
representa el proceso actual.

El código imprime el nombre del proceso, su identificador de proceso (pid) y si 
el proceso está vivo o no en cada iteración.

El código también pasa un nombre a cada proceso en lugar de un argumento, 
es decir, "ana0", "ana1", "ana2".

El resto del código es similar al código anterior, incluyendo la creación de una 
lista "lp" de objetos de proceso, la inicialización de todos los procesos en la 
lista "lp" y la creación y ejecución de un proceso "q" que ejecuta la función "g".

Es importante notar que, debido a que los procesos son ejecutados en paralelo, 
el orden en que aparecen las impresiones "hola soy" y "adios" no está garantizado y 
puede variar en cada ejecución.

"""


from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value
import time

def f(c):
   for i in range(100):
      temp = c.value + 1
      print (f"hola soy {current_process().pid}, vuelta: {i}, contador: {c.value}")
      time.sleep(0.1)
      c.value = temp

if __name__ == "__main__":
   N = 8
   lp = []
   c = Value('i', 0)
   for i in range(N):
      lp.append(Process(target=f, args=(c,)))

   print ("Valor inicial del contador", c.value)
   for p in lp:
      p.start()