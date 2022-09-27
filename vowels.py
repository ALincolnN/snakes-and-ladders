

'''
This project is aimed at defining a CountVowels() function which takes a string as input, checks the characters in the
    string and builds a list pf all the vowels found inna the string then displays it.
'''
def CountVowels(a):
    b = []

    if len(a) != 0 :
        for i in a:
            if i in ['a','e','i','o','u']:
                b.append(i)

        print(len(b))

    else:
        print('No word entered!!')

input(input('Enter a word:'))
CountVowels(input)

