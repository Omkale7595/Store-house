#Code for checking a number is armstrong or not
n=int(input('Enter a number:'))
x=n
l=[]
math=0
while True:
	a=x%10
	x=int(x/10)
	#print(a,x)
	l.append(a)
	#print(l)
	b=len(l)
	if x<1:
		break
for i in l:
	math += i**b
#print(math)
if n==math:
	print("Is an armstrong number!")
else:
	print("Not an armstrong number!")