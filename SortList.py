


def SortList(opt,l=0):

    l = []
    x = int(input('Input the number of times you want the program to execute: '))

    for y in range(x):
        l.append(int(input('Enter a number to add to the list: ')))

        #l.sort()

    if opt == 'asc':
        l.sort()
        print(l)

    elif opt == 'desc':
        l.sort(reverse=True)
        print(l)

    elif opt == 'none':
        print(l)

    else:
        print('Wrong Sort Option!!')

SortList(input('Enter an option for sorting: '))



