for i in range(5):
	for j in range(5):
		# print("(", i, ",", j, ")", sep="")
		print(f"({i},{j})")

a = [23,12,36,53,19]

for i in enumerate(a):
	print('e: ',i)

for index, value in enumerate(a):
	print(index, value)

if all(60>x for x in a) :
	print("True")
else :
	print("False")

if all(50>x for x in a) :
	print("True")
else :
	print("False")

if any(50>x for x in a) :
	print("True")
else :
	print("False")