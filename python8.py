#Suponga que usted es un científico de la computación/ladrón de arte que se ha colado en una galería de arte importante.
#Todo lo que tiene con usted para sacar las obras de arte robadas es su mochila que sólo puede contener libras de arte; n
#o obstante, para cada pieza de arte usted conoce su valor y su peso. Escriba una función de programación dinámica para ayudarse 
#a maximizar sus ganancias. He aquí un ejemplo del problema que usted puede usar para empezar: 
#Supongamos que su mochila aguanta un peso total de 20. Usted tiene 5 ítems como sigue:

class Item:
	def __init__(self, theID, theValue, theWeight):
		self.ID = theID
		self.value = theValue
		self.weight = theWeight

def dpMaxProfit (itemList, knapWeight, maxProfits, weightsUsed):
	maxProfit = 0

	for knapWeights in range (knapWeight + 1):
		print "WEIGHT:", knapWeights - 1, " ", maxProfits
		newItem = itemList[0]

		for item in [x for x in itemList if x.weight <= knapWeights]:
			if maxProfits[knapWeights - item.weight] + item.value > maxProfit: 
				maxProfit = maxProfits[knapWeights - item.weight] + item.value
				newItem = item
		maxProfits[knapWeights] = maxProfit
		weightsUsed[knapWeights] = newItem.weight

	return(maxProfits[knapWeight])
	
def reMaxProfit(itemList, knapWeight):
	if knapWeight < 1:
		return 0 

	l1 = [x for x in itemList if x.weight <= knapWeight]	
	profitList = [(item.value + reMaxProfit(itemList, knapWeight-item.weight)) for item in l1]

	if len(profitList) > 0:
		return max(profitList)
	else:
		return 0 
		
def _weightsUsed(weightList, knapWeight):
	weight = knapWeight
	while weight > 0:
		print(weightList[weight])
		weight -= weightList[weight]
recurse = True
if recurse:
	maxProfits = [0] * (knapWeight + 1)
	weightsUsed = [0] * (knapWeight + 1)

def main():
	itemList = [StolenItem(1,3,2), StolenItem(2,4,3), StolenItem(3,8,4), StolenItem(4,8,5), StolenItem(5,10,9)]
	knapWeight = 20
	if !recurse:
	maxProfits = [0] * (knapWeight + 1)
	weightsUsed = [0] * (knapWeight + 1)
	print(dpMaxProfit(itemList, knapWeight, maxProfits, weightsUsed))
	print weights(weightsUsed, knapWeight)
else:	
print (reMaxProfit(itemList, knapWeight))

if __name__ == "__main__":
	main()