import pytest
import random



spielset = {'stein': 1, 'schere': 2, 'papier': 3}
#1 - 2 / 2 - 3 / 3 - 1 (gewinne)

def sss(text1, text2):
	text1 = text1.lower()

	if spielset[text1] == text2:
		return "Unentschieden!"

	elif spielset[text1] == 1 and text2 == 2:
		return sieger_m()

	elif spielset[text1] == 1 and text2 == 3:
		return sieger_c()

	elif spielset[text1] == 2 and text2 == 3:
		return sieger_m()

	elif spielset[text1] == 2 and text2 == 1:
		return sieger_c()

	elif spielset[text1] == 3 and text2 == 1:
		return sieger_m()

	elif spielset[text1] == 3 and text2 == 2:
		return sieger_c()
	

def start_spiel():
	zufall = random.randint(1,3)
	user_input = input("Geben sie Stein, Schere oder Papier ein: ")
	auswahl = user_input
	print(sss(auswahl, zufall))

def sieger_m():
	return "Mensch gewinnt!"

def sieger_c():
	return "Computer gewinnt!"



def test_user_stein_cmp_schere():
	assert sss("stein", "schere") == "Mensch gewinnt!"

def test_cmp_stein_user_schere():
	assert sss("schere", "stein") == "Computer gewinnt!"

def test_user_papier_cmp_stein():
	assert sss("papier", "stein") == "Mensch gewinnt!"

def test_cmp_papier_user_stein():
	assert sss("stein", "papier") == "Computer gewinnt!"

def test_user_schere_cmp_papier():
	assert sss("schere", "papier") == "Mensch gewinnt!"

def test_cmp_schere_user_papier():
	assert sss("papier", "schere") == "Computer gewinnt!"

if __name__ == '__main__':
	start_spiel()