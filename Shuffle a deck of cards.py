import itertools as iter ,random as r
deck=list(iter.product(range(1,14),['Spade','Heart','Club','Diamond']))
r.shuffle(deck)
for i in range(5):
	print(deck[i][0],deck[i][1] )