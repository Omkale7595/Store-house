def fibonacci_less_than(n):
   
    i = 1
    j = 0
    
    while i < n:
        while j < n:
            i = i + j 
            print(i,end=' ')
            j = i + j 
            print(j,end=' ')
     
fibonacci_less_than(22)