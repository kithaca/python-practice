def deep_dup(li):
	res = []
	for el in li:
		if type(el) is list:
			res = res + deep_dup(el)
		else:
			res.append(el)

	return res

print deep_dup([1, [2], [3, [4]]])