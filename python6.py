
#Escriba un programa que resuelva el siguiente problema: Tres misioneros y tres caníbales llegan a un río y encuentran un
#  bote con capacidad para dos personas. Todos deben cruzar el río para continuar en el viaje. Sin embargo, 
# si los caníbales sobrepasan en número a los misioneros en cada orilla, los misioneros serán comidos. 
# Encuentra una serie de cruces que llevarán a todos a salvo al otro lado del río.


#Primero consideremos que tanto los misioneros (M) como los caníbales (C) están en el mismo lado del río.
#Izquierda derecha
#Inicialmente las posiciones son: 0M, 0C y 3M, 3C (B)

#Ahora enviemos 2 caníbales a la izquierda del banco: 0M, 2C (B) y 3M, 1C

#Envía un caníbal de izquierda a derecha: 0M, 1C y 3M, 2C (B)

#Ahora envía los 2 caníbales restantes a la izquierda: 0M, 3C (B) y 3M, 0C
#Envía 1 caníbal a la derecha: 0M, 2C y 3M, 1C (B)




#Ahora envíe 2 misioneros a la izquierda: 2M, 2C (B) y 1M. 1C

#Envía 1 misionero y 1 caníbal a la derecha: 1M, 1C y 2M, 2C (B)

#Envía 2 misioneros a la izquierda: 3M, 1C (B) y 0M, 2C

#Envía 1 caníbal a la derecha: 3M, 0C y 0M, 3C (B)

#Envía 2 caníbales a la izquierda: 3M, 2C (B) y 0M, 1C

#Envía 1 caníbal a la derecha: 3M, 1C y 0M, 2C (B) "

#Envía 2 caníbales a la izquierda: 3M, 3C (B) y 0M, 0C

#• Aquí (B) muestra la posición del barco después de que se realiza la acción.
#Por tanto, todos los misioneros y caníbales han cruzado el río a salvo.
