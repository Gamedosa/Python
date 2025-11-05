'''
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
'''

person = {"Name": 'Gabriel', "Age": 24}
print(person)

person2 = dict(Name='Julio', Age=24)
print(person2)

# add a new key
person['LastName'] = 'Santos'
print(person)

