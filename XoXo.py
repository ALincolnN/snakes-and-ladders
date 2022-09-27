'''
The program is built to take a string as input,check the characters in the string and return a dictionary of all the Os
    and Xs in the string.

The program then takes the two derived lists,checks the lengths and returns True or False based on if they are equal
    or not.
'''
def check(cross):

    x = []
    o = []
    countX = 0
    countO = 0

    for z in cross:
        if z == 'x':
            x.append(z)
        elif z == 'o':
            o.append(z)

    #print(x)
    #print(o)
    for i in x:
        countX += 1

    for j in o:
        countO += 1

    if countX == countO:
        print(countO == countX)

    else:
        print(countO == countX)

string = input('Enter a word or sentence to check: ')
check(string)


