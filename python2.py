# Escriba una función recursiva para invertir una lista.
# Python Program to Reverse a List using Recursion

def reverse_list(NumList, a, b):
    if(a < b):
        temp = NumList[a]
        NumList[a] = NumList[b]
        NumList[b] = temp
        reverse_list(NumList, a + 1, b-1)

NumList = []
Number = int(input("Enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Enter the Value of %d Element: " %a))
    NumList.append(value)

print("\nOriginal List: ",NumList)

reverse_list(NumList, 0, Number - 1)
print("\nThe Result of a Reverse List =  ", NumList)
#Primero definiremos una lista y luego imprimiremos la lista ingresada por el usuario
#spanish
#def reverse_list (NumList, a, b):
 #   si (a <b):
       # temp = NumList [a]
       # NumList [a] = NumList [b]
        #NumList [b] = temp
        #reverse_list (NumList, a + 1, b-1)

#NumList = []
#Number = int (input ("Ingrese el número total de elementos de la lista:"))
#para i en el rango (1, Número + 1):
   # value = int (input ("Ingrese el valor de% d elemento:"% a))
   # NumList.append (valor)

#print ("\ nLista original:", NumList)

#reverse_list (NumList, 0, Número - 1)
#print ("\ nEl resultado de una lista inversa =", NumList)
