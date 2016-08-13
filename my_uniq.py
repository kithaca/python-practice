def my_uniq(li):
	dups = set()
	res = []
	for x in li:
		if not x in dups:
			res.append(x)
			dups.add(x)

	return res

print my_uniq([1, 1, 2, 3, 4, 4, 5, 6, 7, 7, 2])
