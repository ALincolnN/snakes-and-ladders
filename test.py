
number = int(input("Enter a number: "))

'''
if number%2 ==0:
    print('\n'+str(number) + " is an even number.\n")
else:
    print('\n'+str(number) + " is an odd number.\n")

print("Is your number above divisible by 4?\n")

'''

if number%4 == 0 and number%2 ==0:
    print(str(number) +" is even and divisible by 4.\n")
else:
    print(str(number) + " is odd and not divisible by 4.\n")

print('Now, lets do another test...\n')

num = int(input('Please input another Random number: '))
check = int(input('Now, give a number that you want to divide the above number with: '))

if num%check == 0:
    print('\n'+str(check)+' Divides evenly into '+str(num))

else:
    print('\n'+str(num)+' Isn\'t evenly divided by '+str(check))




