
def calc(num1,op,num2):





    if op == '+':
        sum = num1+num2
        print('The sum is '+str(sum))

    elif op == '-':
        result = num1-num2
        print('The result is '+str(result))

    elif op == '/':
        division = num1/num2
        print(str(num1)+' divided by '+str(num2)+' is '+str(division))

    elif op == '*':
        product = num1*num2
        print('The product of your numbers is: '+ str(product))

    else:
        print('Ooh snapp!! We couldn\'t quite get what you want us to do')


calc(num1 = int(input('Enter the first number: ')),op = input('\nWhat operation do you want applied on the numbers?: '),num2 = int(input('\nNow, enter the second number: ')))