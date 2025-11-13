#Fibonacci series using the range
start=int(input("Enter the start of the range:"))#Taking inputs of start and end limit for the the loop
end=int(input("Enter the end of the range:"))
for i in range(start,end):
	x=i #we count the size of the numbers uisng length function after converting it into the string and then converting back to integer
	s=0
	x=str(x)
	d=int(len(x))
	#print(d)
	x=int(x) #loop to calculate the the required fibonacci series
	while (x>0):
		c=x%10
		x=int(x/10)
		s+=c**d #lastly printing the series
	if (s==i):
		print(s,end=' ')