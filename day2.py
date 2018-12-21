#numbers, you can add, multiply, divide and subtract
# integers 1.....3.....5.....5
# floats a number with a decimal point
# avoiding type errors with the str() Function

age = 23
message = "Happy " + str(age) + "rd Brithday!"
print(message)


print(5 + 3)
print(5 - 3)
print(5 / 3)
print(5 * 3)

number = 7
message2 = "My favorite number is " + str(number)
print(message2)

import this

# What is a list? Is a collection of items in a particular order. 

bikes = ["trek", "cannondale", "redline", "specialized"]
print(bikes[1])
#to print any of the brand you need to call it. List starts in 0 to n
#index positions start at 0, not 1
print(bikes[-1]) #print the end item in the index

message3 = "My first bike was " + bikes[0].title() + ","
print(message3)

names = ["pedro", "juan", "perico"]
message4 = "Hello, " + names[0].title() + "!"
message5 = "Hello, "+ names[1].title() + "!"
message6 = "Hello, "+ names[2].title() + "!"

print(message4)
print(message5)
print(message6)


# the method append() will add different elements to a list

motorcycle = []
motorcycle.append("honda")
motorcycle.append("suzuki")
motorcycle.append("ford")
print(motorcycle)

#How to modify a list?
# using the .insert() method.

motorcycle = ["honda", "yamaha", "suzuki"]
motorcycle.insert(2, "ferrari")
print(motorcycle)

#how to remove a variable?
del motorcycle[0]
print(motorcycle)

#tryityourself

dinner = ["pepe", "caroline", "rafael"]
print("Come home for dinner " + dinner[0] + "!")
print("Come home for dinner " + dinner[1] + "!")
print("Come home for dinner " + dinner[2] + "!")
print(dinner[1] + "will not come for dinner!")

dinner.insert(1, "Pedro")
print(dinner)

print("Come home for dinner " + dinner[0] + "!")
print("Come home for dinner " + dinner[1] + "!")
print("Come home for dinner " + dinner[2] + "!")

dinner.insert(0, "Loreto")
dinner.insert(2, "Mike")
dinner.append("Mike")

print(dinner)














