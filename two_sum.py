def two_sum(li):
	res = []
	idx = 0
	while idx < len(li) - 1:
		curr = li[idx]
		for i, val in enumerate(li[idx + 1:]):
			if curr != val and curr + val == 0:
				res.append([idx, idx + i + 1])
		idx += 1

	return res

print two_sum([-1, 0, 2, -2, 1]) # => [[0, 4], [2, 3]]
print two_sum([-5, 5, 3, 7, -3, 16, 0, 0, 5]) # => [[0, 1], [0, 8], [2, 4]]