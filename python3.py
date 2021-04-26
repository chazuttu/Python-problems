#Escriba una función recursiva para calcular la secuencia de Fibonacci. ¿Cómo se compara el desempeño de la función recursiva con el de una versión iterativa?

# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10
if nterms <= 0:
   print("enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))
#Una secuencia de Fibonacci es la secuencia entera de 0, 1, 1, 2, 3, 5, 8 ....

#Los dos primeros términos son 0 y 1. Todos los demás términos se obtienen sumando los 
#dos términos anteriores. Esto significa que el enésimo término es la suma de (n-1) ésimo y (n-2) ésimo término.
#almacenamos el número de términos que se mostrarán en nterms.

#Se utiliza una función recursiva recur_fibo () para calcular el enésimo término de la secuencia.
 #Usamos un bucle for para iterar y calcular cada término de forma recursiva
#Spanish
#def recur_fibo (n):
  # si n <= 1:
      # volver n
   #demás:
      # return (recur_fibo (n-1) + recur_fibo (n-2))

#ntérminos = 10
#si ntérminos <= 0:
   #print ("ingresa un entero positivo")
#demás:
   #print ("secuencia de Fibonacci:")
  # para i en rango (nterms):
       #imprimir (recur_fibo (i))


