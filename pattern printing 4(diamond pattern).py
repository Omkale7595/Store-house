n=1
for i in range(1,10,2):
	for j in range(15,i,-1):
		print(end=' ')
	for k in range(1,i+1):
		print(n,end=' ')
	n+=1
	print()
for i in range(7,0,-2):
	for j in range(15,i,-1):
		print(end=' ')
	for j in range(1,i+1):
		print(n,end=' ')
	n+=1
	print()