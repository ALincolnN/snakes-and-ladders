'''
import numpy as np

a = [1,2,3,4,5,6,7,8,9,10,11]

b = np.array_split(a,3)

for i in b:
    print(list(i))
'''

my_list = [1, 2, 3, 4, 5,
           6, 7, 8, 9,11,12,'l',5,4,5]


for i in range(0, len(my_list),3):

    y=my_list[i:i+3]
    y.reverse()

    print(y)


