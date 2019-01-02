#exercise from the book "The Python Workbook"
"""
#exercise1
print("Pedro Blanco")
print("The White House" \
"1600 Pennsylvania Avenue NW" \
"Washington, DC 20500")

#exercise2
user_input = input("Please, enter your name")
print("Bienvenido a casa, " + user_input)

#exercise3
user_width = input("Please, enter the width")
user_lenght = input("Please, enter the lenght")

area_room = (user_width ** user_lenght)

print("The area of the room is ", area_room)

#exercise 1

num1 = input("Please, write a number 1: ")
num2 = input("Please, write a number 2: ")

def maxNumber(num1,num2):
	if num1 > num2:
		return print(num1)
	else:
	 	return print(num2)
print(maxNumber(num1,num2))

exercise 2

name = input("Please, enter your name")
address = input("Please, enter your address")
number = input("Please, enter your number")

list = [name, address, number]

print("The personal data is: " + str(list))

"""
"""
# exercise 3

num1 = float(input("Please, write a number 1: "))
num2 = float(input("Please, write a number 2: "))
num3 = float(input("Please, write a number 3: "))

arit = ((num1 + num2 + num3)/3)
print("Aritmethic is: " + arit)

"""

"""email = False
for i in "pedblasangmail.com":
	if (i=="@"):
		email = True
if email == True:
	print("Email correct")
else:
	print("Email not correct")

name = "pedro"
for i in range(len(name)):
	print("Hiiiii")
"""
"""
countries = ["Sevilla", "Madrid", "Barcelona", "Málaga", "Valencia"]
print(countries)
print(sorted(countries))
print(countries)
print(countries.sort(reverse=False))
print(sorted(countries,reverse=True))
print(countries)
print(countries.reverse())


# Working with lists and loopings
cities = ["Paris", "Madrid", "Rome","Barcelona"]
for city in cities:
	print(city)

print(cities[2:3])
cities.append("New York")
print(cities)
squares = [10**2 for value in range(1,11)]
print(squares)

import time
import sys

toolbar_width = 40

# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in xrange(toolbar_width):
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write("-")
    sys.stdout.flush()

sys.stdout.write("\n")



def devuelve_ciudades(*ciudades):
	for elemento in ciudades:
		for subElemento in elemento:
			return subElemento
ciudades_devueltas = devuelve_ciudades("Madrid", "Sevilla", "Paris")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))


def generador(*args):
	for valor in args:
		yield valor * 10 #unejemplo

for valor in generador(1, 2, 3, 4):
	print(valor)



#if you need to use some class, you need it to import from a library
#in this case, we will use .sqrt from the import math library

import math

def calculaRaiz(num1):
	if num1<0:
		raise ValueError ("El número no puede ser negativo")
	else:
		return math.sqrt(num1)

print(calculaRaiz(-1))
"""

#introduction to OOP

class Coche():
	largoChasis = 250
	anchoChasis = 120
	ruedas = 4
	enmarcha = False

	#def función que no pertence a ninguna clase
	#defs método que pertecene a la class Coche()

	def arrancar(self):
		self.enmarcha = True
	
	def estado(self):
		if(self.enmarcha):
			return "El coche está en marcha"
		else:
			return "El coche está parado"

miCoche = Coche()

print(miCoche.largoChasis)
print("El coche tiene ", miCoche.ruedas, " ruedas")
miCoche.arrancar()

print(miCoche.estado())


