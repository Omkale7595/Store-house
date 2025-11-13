a,b=0,1
l=[]
for i in range(1,7):
	l.append(a)
	for j in range(13,i,-1):
		print( end=' ') 
	for k in l:
		print(k,end=' ')
	a,b=b,a+b
	print()