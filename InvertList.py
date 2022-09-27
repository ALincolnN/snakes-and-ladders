'''
The projects aims at taking a string, converting the string to a list, breaking the list into chunks of three and
    finally reversing each list returned and printing it using the invert() function.

'''

my_list = [1, 2, 3, 4, 5,
           6, 7, 8, 9,11,12,'l',5,4,5]


def invert(l):
    for i in range(0, len(l),3):

        y=my_list[i:i+3]
        y.reverse()

        print(y)

my_list = list(input('Please enter a string or characters in any desired order: '))
invert(my_list)
