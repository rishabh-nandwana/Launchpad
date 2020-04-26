mydict = {"hello" : "world", "speckbit" : "self-learning", "life" : "meaning"}
m = mydict.items()
v = input("Enter value: ")
for key,value in m:
	if value == v:
		print(key)
	

