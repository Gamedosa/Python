# Program to calculate user's decade. The goal is to implement the concepts learned.

age = int(input('How old are you?\n'))
decades = age // 10
years   = age % 10
print("You are " + str(decades) + " decades and " + str(years) + " years old.")

