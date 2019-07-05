import requests
import json
import datetime
import dateutil.parser

def abfrage():
	r = requests.get("https://start.vag.de/dm/api/v1/abfahrten/VGN/{}".format('1504'))
	return r.json()

def format_zeit(zeit):
	zeit_obj = dateutil.parser.parse(zeit)	
	return zeit_obj.strftime("%H:%M:%S")

def ausgabe(antwort, produkt_eingabe, richtung_eingabe):
	for x in antwort['Abfahrten']:
		produkt_ist = x['Produkt']
		richtung_ist = x['Richtungstext']
		if produkt_eingabe.lower() == produkt_ist.lower():
			abfahrt_soll = format_zeit(x['AbfahrtszeitSoll'])
			abfahrt_ist = format_zeit(x['AbfahrtszeitIst'])
			if richtung_eingabe == x['Richtungstext'].lower() or not richtung_eingabe:
				print("{}, {}, soll: {}, ist: {}".format(richtung_ist, produkt_ist, abfahrt_soll, abfahrt_ist))


if __name__ == '__main__':
	produkt_eingabe = input('Geben Sie bitte an ob sie UBahn oder Busverbindungen finden wollen: ')
	richtung_eingabe = input('Geben Sie bitte an ob Sie in Richtung Langwasser Süd oder Fürth Hardhöhe fahren wollen: ')	
	richtung_eingabe = richtung_eingabe.lower()
	if not richtung_eingabe in ['Langwasser Süd'.lower(), 'Fürth Hardhöhe'.lower()]:
		richtung_eingabe = None
	antwort = abfrage()
	if antwort:
		ausgabe(antwort, produkt_eingabe, richtung_eingabe)
	else:
		print("Keine Antwort vom Server.")