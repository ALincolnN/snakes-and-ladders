'''
This project is aimed at inspecting a string that the user inputs, and returning the index of all the capital letters in
    the string, implemented using the capital_indexes function that takes one argument, the string.
'''

def capital_indexes(s):
    l = []


    for i in s:
        if i.isupper():
            l.append(s.index(i))
    return l


s = input('Enter a word: ')
print(capital_indexes(s))