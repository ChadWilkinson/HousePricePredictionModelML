#/// Type de variables
monInt = 12
monFloat = 12.12
monString = "Chad"
monBool = True
maListe = [2, 2, 2, 2]
mesCoordonnees = (1, 2)
monDictionnaire = {"prenom": "Chad", "nom": "Wilkinson", "age": 21}
monSet = {2, "allo", False}
monRange = range(10)
monNone = None
#et autres

#/// Boucles
#For loop
nombres = [1, 2, 3, 4, 5]
for nombre in nombres:
	print(nombre)
else:
	print("Nous avons fini la boucle")
	
#While loop
i = 1
while i <= 10:
	print(i)
	i += 1

#For loop (parallel)
debuts = ["Py", "Java", "C"]
fins = ["thon", "Script", "#"]
for debut, fin in zip(debuts, fins):
	print(f"{debut}{fin}")
	
#Resultat :
	#Python
	#JavaScript
	#C#

#/// Fonctions & Subroutines
#Functions
def somme(a, b):
	return a+b

#Subroutines
def allo():
	print("allo")

#/// Moins commun
#Dynamic typing
x = 2
print(type(x))	#output: <class 'int'>

x = "allo"
print(type(x))	#output: <class 'str'>

#List comprehensions
mesNombres = [1, 2, 3, 4, 5]
mesNombresCarre = [x**2 for nombre in mesNombres]
print(mesNombresCarre)	#output: [1, 4, 9, 16, 25]

#Duck typing
#As long as it looks, swims and acts like a duck,
#i'll treat it like one.

maString = "chadwilkinson"
maListe = [2, 2, 2, 2]

len(maString)	#output: 13
len(maListe)	#output: 4