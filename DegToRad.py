'''
The function is aimed at converting degrees to radians and returning the result using the DegToRad() function
'''

from math import pi

def DegToRad(num):

    return num * (pi/180)

x = DegToRad(int(input('Please input a number: ')))

print('The converted Degrees to Radians is: ',x)