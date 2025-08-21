def bill_spilt():
     num1 = int(input('Please enter the subtotal amount:'))
     num2 = int(input('Please enter the number of friends:'))
     math1 = num1/100
     math2 = math1 * 20
     math3 = num1 + math2
     math4 = math3 / num2
     rounded_num = round(math4,2)
     print('The total amount needed to pay by each friend is:',rounded_num)
        
bill_spilt()