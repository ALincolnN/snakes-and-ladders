
def discount(mp,d):
    sp = mp*((100-d)/100)
    print('\nThe price after discount is: '+str(sp))


mp = int(input('Enter the Marked price: '))
d = int(input('\nEnter the percentage discount to be applied: '))
discount(mp,d)