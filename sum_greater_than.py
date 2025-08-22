def sum_greater_than(numbers,n):
    total = 0
    #print(numbers)
    #print(n)
    for i in numbers:
        if i <= n:
            continue
            
        total += i
    print('The total is :',total)
    
sum_greater_than([1,2,3,4,5],2)