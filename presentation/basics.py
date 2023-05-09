#/// Type de variables

monInt = 12
monFloat = 12.12
monString = "Chad"
monBool = True
maListe = [8, 8, 8, 8]
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

#Output :
	#1
	#2
	#3
	#4
	#5
	#Nous avons fini la boucle

	
#While loop
i = 1
while i <= 10:
	print(i)
	i += 1

#Output :
	#1
	#2
	#3
	#4
	#5
	#6
	#7
	#8
	#9
	#10

#For loop (parallel)
debuts = ["Py", "Java", "C"]
fins = ["thon", "Script", "#"]
for debut, fin in zip(debuts, fins):
	print(f"{debut}{fin}")
	
#Output :
	#Python
	#JavaScript
	#C#

#/// Fonctions & Subroutines

#Fonctions
def somme(a, b):
	return a+b

somme(1, 2)

#Subroutines
def allo():
	print("allo")

allo()

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
#it'll be interpreted as one.

maString = "chadwilkinson"
maListe = [8, 8, 8, 8]

len(maString)	#output: 13
len(maListe)	#output: 4