'''
Write a Python code to accept a string from the user and display characters present at an even index number.

For example, str = "PYnative". so your code should display p, n, t, v.

'''

def even_index(word):
    
    size = len(word)
    for letter in range(0,size,2):
        print(word[letter])
    
   

even_index('Pynative')
    