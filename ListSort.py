a = [1,2,3,4,'lincoln','njogu',9,12,5,'linkie']

b =[]

for i in a:
    if type(i) == int:
    #if isinstance(i,int):
        b.append(i)

print(b)