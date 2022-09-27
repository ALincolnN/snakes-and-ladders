'''
The project is aimed at getting a list of mixed datatypes as input, sorting integer items from the list and appending
    them to another list and printing them after the iteration.
'''
a = [1,2,3,4,'lincoln','njogu',9,12,5,'linkie']

b =[]

for i in a:
    if type(i) == int:
    #if isinstance(i,int):
        b.append(i)

print(b)