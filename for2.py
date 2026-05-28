for i in range(5):
	for j in range(5):
		# print("(", i, ",", j, ")", sep="")
		print(f"({i},{j})")

a = [23,12,36,53,19]

for i in enumerate(a):
	print(i)

for index, value in enumerate(a):
	print(index, value)