print('This is a non ui calculator.')
print('Instructions : 1-addition,2-substraction,3-multiplication,4-division,5-percentage,6-floor division,7-modulo,8-power')
#from here the loop starts and this is an infinite while loop.
while True :
    
    a=int(input('Enter a number from instructions to calculate: '))
    
    if a == 1:
        print('addition is set')
        num1 = int(input('Enter a first number: '))
        num2 = int(input('Enter a second number: '))
        add = num1 + num2
        print('The answer to the addition problem is : ',add)
        
    elif a == 2:
        print('substraction is set')
        num1 = int(input('Enter a first number: '))
        num2 = int(input('Enter a second number: '))
        sub = num1 - num2
        print('The answer to the substraction problem is : ',sub)
        
    elif a == 3:
        print('multiplication is set')
        num1 = int(input('Enter a first number: '))
        num2 = int(input('Enter a second number: '))
        multi = num1 * num2
        print('The answer to the multiplication problem is : ',multi)
        
    elif a == 4:
        print('division is set')
        num1 = int(input('Enter a first number: '))
        num2 = int(input('Enter a second number: '))
        div = num1 / num2
        print('The answer to the multiplication problem is : ',round(div,2))
        
    elif a == 5:
        print('percentage is set')
        num1 = int(input('Enter a first number: '))
        num2 = int(input('Enter a second number: '))
        percent1 = num1 / num2
        percent2 = percent1 * 100
        print('The answer to the percentage problem is : ',percent2)
        
    elif a == 6:
        print('floor division is set')
        num1 = int(input('Enter a first number: '))
        num2 = int(input('Enter a second number: '))
        floor = float(num1 // num2)
        print('The answer to the floor division problem is : ',floor)    
        
    elif a == 7:
        print('modulo is set')
        num1 = int(input('Enter a first number: '))
        num2 = int(input('Enter a second number: '))
        modu = num1 % num2
        print('The answer to the modulo problem is : ',modu)
        
    elif a == 8:
        print('power is set')
        num1 = int(input('Enter a first number: '))
        num2 = int(input('Enter a second number: '))
        power = num1 ** num2
        print('The answer to the power problem is : ',power)
#if the user entered a number other than specified in the instructions none will be printed
    else :
        print('none')