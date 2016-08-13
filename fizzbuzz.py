def fizzbuzz(li):
	result = []
	for x in li:
		if x % 15 == 0:
			continue
		if x % 3 == 0 or x % 5 == 0:
			result.append(x)
	return result

li = range(1, 101)

print fizzbuzz(li)