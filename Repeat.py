'''
a='123l'

b=''

for i in a:
    b += i+i

print(b)

'''

'''
The aim of this coding challenge is to have a function that doubles each and every character in a string that the user inputs
'''

def repeat(whatever):
    b = ''

    for i in whatever:
        b += 2*i

    return b


question = input('Enter a string you would like it\'s characters doubled: ')

print(repeat(question))
