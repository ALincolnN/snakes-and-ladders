
'''
The project is aimed at taking user inputs like the option to use for sorting, number of times the user should input
    their desired values and then the items to include in the list according to the number of times specified.
    The program will then sort the list according to the option the user has entered.
'''

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
option = input('Enter an option for sorting i.e(desc,asc or none): ')
SortList(option)



