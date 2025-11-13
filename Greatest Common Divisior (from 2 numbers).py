#Program to calculate Greatest Common Divisior
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
max=max(n1,n2)#finding maximum and minimum values
min=min(n1,n2)
divisior_n1=0
divisor_n2=0
no_of_common_divisior=[]
for i in range(1,min+1):
	divisor_n1=max%i
	divisior_n2=min%i
	if (divisior_n1==0 and divisior_n2==0):
		#print(i)
		no_of_common_divisior.append(i)
		GCD=i
print(f"The number of common divisior is {no_of_common_divisior}")
print(f"The Greatest Common Divisior is {GCD}")