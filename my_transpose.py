def my_transpose(matrix):
	transposed = []
	for x in range(0, len(matrix[0])):
		new_row = [None] * len(matrix)
		transposed.append(new_row)

	for row, val1 in enumerate(transposed):
		for col, val2 in enumerate(val1):
			transposed[row][col] = matrix[col][row]

	return transposed


m = [
	    [0, 1, 2, 9],
	    [3, 4, 5, 9],
	    [6, 7, 8, 9]
	]

print my_transpose(m)  # =>
 #	 [[0, 3, 6],
 #    [1, 4, 7],
 #    [2, 5, 8],
 #	  [9, 9, 9]]