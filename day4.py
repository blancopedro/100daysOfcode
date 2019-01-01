#today I am reading some notes about Python, this link https://6009.cat-soop.org/6.145_notes/chapter1
"""
italian = ["pasta", "pizza"]
chinese = ["rice", "tempura"]

dish = input(("Please, enter the name of the dish."))

if dish in italian:
	print(italian)
elif dish in chinese:
	print(chinese)
else:
	print("Please, select a dish")
"""
"""

usa = ["chicago", "baltimore"]
spain = ["madrid", "barcelona"]

country = input("Please, enter a city")

if country in usa:
	print("USA")
elif country in spain:
	print("SPAIN")
elif country in usa:
	if country in usa:
		print("SAME COUNTRY")
	elif country in spain:
		print("DIFFERENTE COUNTRY")
"""

#for loop

exp = [12, 13, 54, 21, 12]
# total = sum[0] + sum[1] + sum[2] + sum[3] + sum[4]
total = 0
for item in exp:
	total = total + item
print(total)


def message():
	print("Lorem ipsum....")

message()


nota_alumno = input("Por favor, introduce una nota")
print("su nota es" + nota_alumno)