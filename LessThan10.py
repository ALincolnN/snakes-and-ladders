'''
The project aims at getting an integer list as an input,checking the items in the list and if the item is less than 5,it appends
    the item to another list which will be displayed after the iteration.
'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = []

for i in a:
    if i < 5:
        b.append(i)

print(b)
