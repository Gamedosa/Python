''' List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc
'''

my_list = ['banana', 'apple']
print(my_list)
pick = my_list[1]
print(pick)

fruit = input('info a fruit : \n')
my_list.append(fruit)
print(my_list)