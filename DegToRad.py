from math import pi

def DegToRad(num):

    return num * (pi/180)

x = DegToRad(int(input('Please input a number: ')))

print('The converted Degrees to Radians is: ',x)