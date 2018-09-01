def getNumbers(n):
	for x in range(n):
		yield x

print(getNumbers(9))	

g = getNumbers(10)
print(g.__next__())
print(g.__next__())
print(g.__next__())