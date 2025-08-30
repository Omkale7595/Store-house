def is_prime(n):
	if n <= 1:
		print(False)
	if n == 2:
		print(True)
		
	for i in range(2,n):
		
		if n % i == 0 :
			 return False
			
	return True
			
print(is_prime())