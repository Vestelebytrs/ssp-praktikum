import pytest
import random


x = random.randint(0, 3)
cmp_auswahl = x

spielset = {"stein": 1, "schere": 2, "papier": 3}
spielset x = ["stein"]
spielset y = ["schere"]
spielset z = ["papier"]
def sss(text1, text2):
	
	if cmp_auswahl == 1:
		if spielset[text1] == 1 and text2 == 1:
			print("Unentschieden.")
		elif text1 == 1 and text2 == 2:
			print("Stein gewinnt.")
		else:
			print("Papier gewinnt.")
	
	 if cmp_auswahl == 2:
		if text1 == 2 and text2 == 1:
			print("Stein gewinnt.")
		elif text1  == 2 and text2 == 2:
			print("Unentschieden.")
		else:
			print("Schere gewinnt.")
	
	if cmp_auswahl == 3:
		if text1 == 3 and text2 == 1:
			print("Papier gewinnt.")
		elif text1 == 3 and text2 ==2:
			print("Schere gewinnt.")
		else:
			print("Unentschieden.")

	
def start_spiel():
	input("Wähle: Stein, Schere, oder Papier")


def test_cmp_schere_user_stein():
	assert sss("schere", "stein") == "Mensch gewinnt!"

def test_user_schere_cmp_stein():
	assert sss("schere", "stein") == "Computer gewinnt!"

def test_cmp_schere_user_papier():
	assert sss("schere", "papier") == "Computer gewinnt!"

def test_user_schere_cmp_papier():
	assert sss("schere", "papier") == "Mensch gewinnt!"

def test_cmp_papier_user_stein():
	assert sss("papier", "stein") == "Computer gewinnt!"

def test_user_papier_cmp_stein():
	assert sss("papier", "stein") == "Mensch gewinnt!"


if __name__ == '__main__':
	start_spiel()