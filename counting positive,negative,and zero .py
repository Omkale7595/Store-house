positive=0
negative=0
zeroes=0
while True:
	n=int(input())
	if n==-1:
		break
	elif (n>0):
		positive+=1
	elif (n<0):
		negative+=1
	else:
		zeroes+=1
print('positives:',positive,'\nnegatives:',negative,'\nzeroes:',zeroes)