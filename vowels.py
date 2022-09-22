
def CountVowels(a):
    b = []

    if len(a) != 0 :
        for i in a:
            if i in ['a','e','i','o','u']:
                b.append(i)

        print(len(b))

    else:
        print('No word entered!!')

CountVowels(input('Enter a word:'))

