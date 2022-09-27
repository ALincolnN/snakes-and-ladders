'''
This project is used to test the number the user inputs and test if it is a prime number.If so, the check function
    returns a 1 and if not it returns -1.
'''
def check(x):
    for i in range(2, x):
        if x%i == 0:
            return -1



    return 1


x=int(input('Please input a number: '))
print(check(x))
