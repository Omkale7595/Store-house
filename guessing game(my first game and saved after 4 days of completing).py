import random
print("-------Welcome to the guessing game!-------")
diff=int(input("Enter the difficulty level(1,2,or3):"))
m=0
if diff == 1:
 	n=list(range(1,21))
 	o=random.choice(n)
 	m=o
 	x=5
 	z=x
 	s=0
 	print("Enter a number from 1-20")
elif diff == 2:
 	n=list(range(1,51))
 	q=random.choice(n)
 	m=q
 	w=10
 	d=15
 	s=d
 	z=w
 	print("Enter a number from 1-50")
elif diff == 3:
 	n=list(range(1,101))
 	p=random.choice(n)
 	m=p
 	y=10
 	r=25
 	s=r
 	z=y
 	print("Enter a number from 1-100")
print(m)
turns,score=10,0
for i in range(10):
	print("Turns:",turns)
	turns-=1
	a=int(input("Enter your number:"))
	if(m==a):
	 print("🎉 -You have won!-Congratulations ")
	 score+=1
	 print(f"Total score {score}")
	 exit()
	elif(m - z < a < m + z):
		print("🔥 🔥 Too close!")
	elif(m - s < a < m + s):
	   print("🔥 Close to right answer")
	elif(a>m):
	  print("Too high!")
	elif(a<m):
	   print("Too low")
print(f"The hidden number was {m}.\n💔You lost")