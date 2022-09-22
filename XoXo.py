
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

    
check(input('Enter a word or sentence to check: '))


