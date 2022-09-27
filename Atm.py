'''
The project aims at getting the input from the user with clear instruction that it should be 12 characters long.

The function mask() then converts the first 8 characters of the string and replaces them with asterisks and only
    reveals the last 4
'''
def mask(cvv):

    x = ''
    l = len(cvv)
    if l == 12:

        for i in cvv and range(l-4):
            x += '*'

        return(x+cvv[7:11])
    else:
        err = 'The required length should be 12 characters!! TRY AGAIN!!'
        return err

code = input('Enter your 12 digit Credit Card Number: ')
print(mask(code))







