n=int(input('Enter a number:'))
x=n
s=0
while (n>0):
	a=n%10
	n=int(n/10)
	s+=a**3
if x==s:
	print("Is an armstrong number!")
else:
	print("Not an armstrong number!")