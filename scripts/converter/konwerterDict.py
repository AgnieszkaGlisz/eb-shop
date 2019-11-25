#!/usr/bin/env python3
import json
import random

file = open("/media/bjank/Data/studia/5 sem/Biznes Elektroniczny/eb-shop-master/data/merlin2.json", "r", encoding='utf-16')
jsonString = file.read()
source = json.loads(jsonString)

nazwa = ""
podsumowanie = ""
kategoria = ""
cena = ""
status = ""
zdjecie = ""
opis = ""
ilosc = ""
ean = ""
autor = ""
przecena = ""
newDict = []

for tup in source:
	for key,value in tup.items():
		if key == "Title":
			nazwa = value
		elif key == "Author":
			podsumowanie = '<font size="5">' + value[:-2] + "</font><br/><br/>"
			autor = value[:-2]
		elif key == "Publisher":
			podsumowanie += "Wydawca: " + value + "<br/>"
		elif key == "Category":
			kategoria = value
		elif key == "Price":
			cena = value
		elif key == "Status":
			status = value
		elif key == "Img":
			zdjecie = "http:" + value
		elif key == "Description":
			opis = value
		elif key == "Discount":
			przecena = value[:-1]
			przecena = przecena[1:]
		elif key == "Informations":
			for k,v in value.items():
				if k == "EAN:":
					ean = v
				if k == "Liczba stron:":
					podsumowanie += "Liczba stron: " + v + "<br/>"
				if k == "Okładka:":
					podsumowanie += "Okładka: " + v + "<br/>"
				if k == "Nr katalogowy:":
					podsumowanie += "Nr katalogowy: " + v + "<br/>"
				if k == "ISBN:":
					podsumowanie += "ISBN: " + v + "<br/>"
				if k == "Data Premiery:":
					podsumowanie += "Data Premiery: " + v + "<br/>"
	ilosc =  random.randint(1, 100) 

	newDict.append({
		'Nazwa':nazwa,
		'Podsumowanie':podsumowanie,
		'Kategoria':kategoria,
		'Cena':cena,
		'Status':status,
		'Zdjecie':zdjecie,
		'Ilosc':ilosc,
		'EAN':ean,
		'Autor':autor,
		'Przecena':przecena,
		'Opis':opis
	})

with open('newMerlin2.json', "w", encoding='utf-16') as file_write:
	json.dump(newDict, file_write, indent=1, sort_keys=False, ensure_ascii=False)

file.close()
