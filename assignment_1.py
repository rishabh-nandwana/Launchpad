user_details = {}
name = []
usn = []
for i in range(3):
	name.append(input("Enter name : "))
	usn.append(input("Enter usn : "))
for i in range(len(usn)):
	user_details[usn[i]] = name[i]
print(user_details)