"""#write addition, subtraction, multiplication and division
print(5+3)
print(11-3)
print(4*2)
print(16/2)

#Pedro Blanco, 08/01/2019

fav_number = 3
text ="My favorite number is" + str(fav_number) + " !!!!"
print(text)

#guessList

list = ["pedro", "john","Charles"]
print(list[0] + ", welcome to our restaurant.")
print(list[1] + ", welcome to our restaurant.")
print(list[2] + ", welcome to our restaurant.")

magicians = ["pedro","john", "eric"]
for magician in magicians:
	print(magician)

pizzas = ["a", "b","c"]
for pizza in pizzas:
	print("I like " + pizza + " pizza")

print("Wonderful pizzas!")"""

number = list(range(11, 17))
print(number)

print(max(number))
print(min(number))
print(sum(number))

print(number[-3:])