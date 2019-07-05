import random

x = random.randint(0,100)

def richtig(ausgabe):
	print("Zahl ist richtig erraten!")

ausgabe = None

def größerkleiner(eingabe):
	if eingabe < x: 
		text = "klein"
	if eingabe > x:
		text = "groß"
	print("Zahl ist zu {}. Versuche erneut.".format(text))

eingabe = None

while x != eingabe:
	eingabe = int(input('Rate meine Zahl: '))
	if eingabe != x:
		größerkleiner(eingabe)
	else:
		richtig(ausgabe)
