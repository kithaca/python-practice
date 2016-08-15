def iterative_fibs(n):
	fibs = [0, 1]
	if n <= 2:
		return fibs[0:n]

	while len(fibs) < n:
		fibs.append(fibs[-2] + fibs[-1])

	return fibs

print iterative_fibs(0)
print iterative_fibs(1)
print iterative_fibs(2)
print iterative_fibs(3)
print iterative_fibs(4)
print iterative_fibs(10)

def recursive_fibs(num):
	fibs = [0, 1]
	if num <= 2:
		return fibs[0:num]

	new_fibs = recursive_fibs(num-1)
	new_fibs.append(new_fibs[-2] + new_fibs[-1])

	return new_fibs

print recursive_fibs(0)
print recursive_fibs(1)
print recursive_fibs(2)
print recursive_fibs(3)
print recursive_fibs(4)
print recursive_fibs(10)