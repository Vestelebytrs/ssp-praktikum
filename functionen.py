import random

x = random.randint(0,7)
y = random.randint(0,7)

def unterschied(vergleich):
	if x > y:
		text = "x ist kleiner = Y"
	if x < y:
		text = "x ist größer = X"
	print("Angabe: {}".format(text))
vergleich = None

def richtig(ausgabe):
	print("Werte sind gleichgroß = XY")
ausgabe = None

if x != y:
	unterschied(vergleich)
else:
	richtig(ausgabe)