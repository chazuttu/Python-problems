# 4.17. Ejercicios de programación
# Escriba una función recursiva para calcular el factorial de un número.
def recur_factorial(n):  
   if n == 1:  
       return n  
   else:  
       return n*recur_factorial(n-1)   
num = int(input("Enter a number: "))   
if num < 0:  
   print("factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is",recur_factorial(num))
#Tomaremos información del usuario, luego verificaremos si el número es negativo o no y luego 
#imprimiremos la declaración en consecuencia.
# Spanish 
#def factor_recurrente (n):
# si n == 1:
   #    volver n
  # demás:
  #     return n * recur_factorial (n-1)
#num = int (input ("Ingresa un número:"))
#si num <0:
   print ("factorial no existe para números negativos")
#elif num == 0:
   #print ("El factorial de 0 es 1")
#demás:
   #print ("El factorial de", num, "es", recur_factorial (num))
