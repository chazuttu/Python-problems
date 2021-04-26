#Escriba un programa que imprima el triángulo de Pascal. Su programa debe aceptar un parámetro que indique cuántas filas del triángulo se imprimirán.



n=int(input("Enter number of rows: "))
a=[]
for i in range(n):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if(n!=0):
        a[i].append(1)
for i in range(n):
    print("   "*(n-i),end=" ",sep=" ")
    for j in range(0,i+1):
        print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
    print()

#El usuario debe ingresar el número de filas que debe tener el triángulo de Pascal.
#El bucle for se utiliza para agregar sublistas a una lista vacía definida anteriormente.
#Luego se agrega 1 a todas las sublistas.
#El bucle for se usa para determinar el valor del número dentro del triángulo, que es la suma de los dos números que están encima.
#El otro bucle for se utiliza para imprimir el triángulo de Pascal según el formato.