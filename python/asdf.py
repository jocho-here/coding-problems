def is_prime(n):
	if n <= 1: return False
	if n == 2: return True
	if n % 2 == 0: return False
 
	# exclusing 2, all primes are odd
	i = 3
	while i*i <= n:
		if n % i == 0:
			print(i)
			return False
		i += 2
	
	return True
