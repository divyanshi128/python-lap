str=input("enter the string:")
a=""
for i in str:
	if i not in a:
		print(i, str.count(i))
		a +=i
	

