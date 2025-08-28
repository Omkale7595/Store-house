def modify_tuple(tupl,elem):
	
	tupl=list(tupl)
	print(type(tupl))
	tupl.extend(elem)
	print(tupl)
	
modify_tuple((1,2,3),[4,5,6,7,8])