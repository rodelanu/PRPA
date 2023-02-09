
"""

Este código utiliza la biblioteca "multiprocessing" de Python para crear y 
controlar múltiples procesos.

La función "f" recibe un objeto "c" como argumento, que es un objeto "Value" de 
la biblioteca "multiprocessing". Un objeto "Value" permite la compartición de un 
valor entre procesos. La función "f" aumenta el valor de "c" en 1 en cada iteración y 
lo imprime junto con el identificador de proceso (pid) y el valor de "i".

El código crea una lista "lp" de 8 objetos de proceso, cada uno de los cuales 
ejecuta la función "f" con el objeto "c" como argumento. Todos los procesos en 
la lista "lp" son iniciados y se espera que terminen con "p.join()".

El código también crea un proceso "q" que ejecuta la función "g", y se espera 
que termine con "q.join()".

El valor inicial y final del objeto "c" es impreso antes y después de la ejecución 
de todos los procesos. Debido a que los procesos están modificando el valor de "c" 
de manera concurrente, es probable que el valor final sea diferente al valor inicial.

Es importante notar que, debido a la naturaleza concurrente de los procesos, 
el orden en que aparecen las impresiones "hola soy" y "adios" no está garantizado y 
puede variar en cada ejecución.

"""

from multiprocessing import Process
from multiprocessing import current_process
from multiprocessing import Value

def f(c):
   for i in range(100):
      c.value = c.value + 1
      print (f"hola soy {current_process().pid}, value: {i}, contador: {c.value}")

def g():
   print ("adios")

if __name__ == "__main__":
   N = 8
   lp = []
   c = Value('i', 0)
   for i in range(N):
      lp.append(Process(target=f, args=(c,)))
   print (f"Valor inicial del contador {c.value}")
   for p in lp:
      p.start()

   for p in lp:
      p.join()

   q = Process(target=g)
   q.start()
   q.join()
   print (f"Valor final del contador {c.value}")
   print ("fin")