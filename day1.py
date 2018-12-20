#day1, I will write some code by myself and notes. I am using the book "Python Crash course by Eric Matthes"

print("Hello, universe!")

message = "Hello, Spain!"
print(message)

# student_name is a good way to name a variable
# studentname is a bad way to name a variable

#Be careful with spelling mistakes, for example, mesage instead of message

# mesage2 = "Bonjour"
# print(message2)

#Strings: series of characters

"Hola, mundo!"

name = "peter white"
print(name.title())
# name of the variable + title will print your string in capital letters

# Other ways

print(name.upper()) # all CAPITAL LETTER
print(name.lower()) # LOWER

# Combine different strings

combine1 = "Peter"
combine2 = "White"
mix = combine1 + " " + combine2 
print(mix)

 #method rstrip(), python will check if there is any blank space in the right part of the sentence

space = "Peter "
print(space.rstrip())

#Sintax error with apostrophe. Differente " one of python's strengths " vs  ' one of python's strengths '
#The first one is correct for Python, but, the second one Python with close the first ''

#Try it yourself excercises
#2-3
name = "John"
print("Hello "+ name + ", what a wonderfull day!")

#2-4
print(name.upper())
print(name.lower())
print(name.title())
#2-5
murakami_quote = "“If you only read the books that everyone else is reading, you can only think what everyone else is thinking."
name2 = "Murakami"
print(murakami_quote + " by " + name2)

