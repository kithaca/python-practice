def my_each(li, fn):
	res = []
	for x in li:
		res.append(fn(x))

	return res

print my_each([1, 2, 3, 4], lambda x: x * 2)
