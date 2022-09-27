'''
This project is basically aimed at getting an input from the user and use it as a range to display all the
    prime numbers between 2 and the number the user input.
It is implemented using to functions;
    a)The check function to check for the prime nature of the number,
    b)The inp function to get the input from the user and pass the corresponding numbers to the Check function
        to check if the passed number is prime, Then print the prime numbers in a list.
'''

def check(x):
    for i in range(2, x):
        if x%i == 0:
            return -1



    return 1

def inp(j):
    p=[]
    if j>1:
        for i in range(2, j):
            if check(i) == 1:
                p.append(i)
        return p
    else:
        return 'The number you input is less than 1'


x=int(input('Please input a number: '))
print(inp(x))
