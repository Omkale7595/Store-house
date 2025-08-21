'''def pass_fail():
    score = int(input('Please enter your score: '))
    if score >=50:
        print('The candidate has passed.')
        
    else :
        print('The candidate has failed.')   
        
pass_fail() ''
def pass_fail(score):
    if score >= 50 :
        print('The candidate has passed.')
        
    else :
        print('The candidate has failed.')
        
pass_fail(50)
pass_fail(60)
pass_fail(40)       '''
'''languages = ('Swift', 'Python', 'Go')

# access elements of the list one by one
for lang in languages:
    print(lang)
Toss = 'Heads'
for x in Toss :
    print(x)
    # iterate from i = 0 to 3
for _ in range(0,4):
    print('Hi')
    print(10)'''
def factorial(n):
    factorial = 1
    for i in range(1,n+1):
        factorial *= i
        
    print('The factorial is : ',factorial)
factorial(5)        