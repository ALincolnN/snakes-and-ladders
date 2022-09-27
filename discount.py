'''
Using the discount() function, this project is aimed at getting the user input on the marked price of an item, the
    percentage discount to be applied and finally returns the calculated selling price of the item and the discount
    applied.
'''
def discount(mp,d):
    sp = mp*((100-d)/100)
    print('\nThe price after discount is: '+str(sp))


mp = int(input('Enter the Marked price: '))
d = int(input('\nEnter the percentage discount to be applied: '))
discount(mp,d)