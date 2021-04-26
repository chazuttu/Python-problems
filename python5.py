#Escriba un programa para resolver el siguiente problema: Usted tiene dos jarras: una jarra de 4 galones y una jarra de 3 galones. Ninguna de las jarras tiene marcas en ella. Hay una bomba que se puede utilizar para llenar las jarras con agua
#.¿Cómo se pueden obtener exactamente dos galones de agua en la jarra de 4 galones?

def gcd(a, b):
	if b==0:
		return a
	return gcd(b, a%b)

def Pour(toJugCap, fromJugCap, d):


	fromJug = fromJugCap
	toJug = 0

	
	step = 1
	while ((fromJug is not d) and (toJug is not d)):

		
		temp = min(fromJug, toJugCap-toJug)

		
		toJug = toJug + temp
		fromJug = fromJug - temp

		step = step + 1
		if ((fromJug == d) or (toJug == d)):
			break

		t
		if fromJug == 0:
			fromJug = fromJugCap
			step = step + 1

		
		if toJug == toJugCap:
			toJug = 0
			step = step + 1
			
	return step


def minSteps(n, m, d):
	if m> n:
		temp = m
		m = n
		n = temp
		
	if (d%(gcd(n,m)) is not 0):
		return -1
	
	
	return(min(Pour(n,m,d), Pour(m,n,d)))


if __name__ == '__main__':

	n = 3
	m = 5
	d = 4

	print('Minimum number of steps required is',
							minSteps(n, m, d))
	#Podemos llenar una jarra con la bomba.
#Podemos verter agua de una jarra al suelo.
#Podemos verter agua de una jarra a otra.
#No hay ningún dispositivo de medición disponible.

