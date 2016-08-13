def is_prime(n):
	if n < 2:
		return False
	elif n == 2:
		return True

	for x in range(2, n):
		if n % x == 0:
			return False

	return True

# print is_prime(1)
# print is_prime(2)
# print is_prime(5)
# print is_prime(303)
# print is_prime(541)


def first_n_primes(n):
	res = []
	curr = 2
	while len(res) < n:
		if is_prime(curr):
			res.append(curr)
		curr += 1

	return res

# print first_n_primes(0)
# print first_n_primes(1)
# print first_n_primes(10)
# print first_n_primes(50)

def sum_of_n_primes(n):
	li = first_n_primes(n)
	return reduce(lambda x, y: x + y, li)

# print sum_of_n_primes(5)