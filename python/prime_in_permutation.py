# Find prime numbers among permutations of given integers
#
# Sieve of Eratosthenes: why only calculate upto sqrt(n)?
#   - https://math.stackexchange.com/questions/58799/why-in-sieve-of-erastothenes-of-n-number-you-need-to-check-and-cross-out-numbe
#1. regular permutation creation + regular trial division
#- 25.20s user 0.17s system 99% cpu 25.505 total 
#- Answer size: 43089
#
#2. modified permutation creation + modified trial division
#- 13.50s user 0.06s system 99% cpu 13.577 total
#- Answer size: 43090
#
#3. modified permuttion creation + set theory for prime & perms to find intersection
#- 46.11s user 2.33s system 99% cpu 48.617 total
#- Answer size: 43088

odds = []
evens = []
perms = set([])
up_to = []
answer = set([])
list_int = []

def primes_sieve(limit):
	global up_to
	ds = [True] * limit
	ds[0] = ds[1] = False

	for i in range(int(limit**0.5) + 1):
		if ds[i] == True:
			for n in xrange(i*i, limit, i):
				ds[n] = False
	
	for i in range(len(ds)):
		if ds[i] == True:
			up_to.append(i)

# Regular trial division
def is_prime_regular(n):
	if n <= 1: return False
	if n == 2: return True
	if n % 2 == 0: return False
	
	i = 3

	while i * i <= n:
		if n % i == 0:
			return False
		i += 2 
	
	return True

# Modified trial division
def is_prime_modified(n):
	if n <= 1: return False
	if n == 2: return True
	if n % 2 == 0: return False
	
	i = 0

	while i < len(up_to) and up_to[i] * up_to[i] <= n:
		if n % up_to[i] == 0:
			return False
		i += 1
	
	return True

def find_primes_regular():
	global perms
	global list_int

	for i in range(len(list_int)):
		temp = list_int.pop(i)
		create_permutations_regular(str(temp))
		list_int.insert(i, temp)
	
	#print('created perms', len(perms))

	# Find primes
	# Use regular triad division
	
	for i in perms:
		if is_prime_regular(i):
			answer.add(i)
	
	#print('len(answer)', len(answer))

def find_primes_experimental():
	global perms
	global odds
	global evens
	global list_int

	# Dividing between odds and evens
	for i in list_int:
		if i % 2 == 1:
			odds.append(i)
		else:
			evens.append(i)

	if 2 in evens:
		perms.add(2)
	
	if 3 in odds:
		perms.add(3)

	# Backtracking; only place odd number at the last digit
	# since even numbers are not primes obviously
	for i in range(len(odds)):
		temp = odds.pop(i)
		if temp != 5:
			create_permutations_modified(str(temp))
		else:
			perms.add(5)
		odds.insert(i, temp)
	
	#print('created perms', len(perms))

	# Compute a list of prime numbers up to sqrt(largest permutation)
	# Use Sieve of Eratosthenes 
	largest = 0

	for i in perms:
		if i > largest:
			largest = i
	
	#print('largest among perms', largest)

	print(1)
	# Get primes upto largest
	primes_sieve(largest)
	print(2)

	#print('primes_sieve up to', int(largest**0.5))
	#print('length of up_to', len(up_to))

	# A U B = A + B - A  B -->
	# A  B = A + B - A U B
	print(3)
	S = {}
	for i in up_to:
		S[i] = 1
	print(4)
	for i in perms:
		if i in S:
			answer.add(i)
	print(5)
	
	print(len(answer))

def find_primes_modified():
	global perms
	global odds
	global evens
	global list_int

	# Dividing between odds and evens
	for i in list_int:
		if i % 2 == 1:
			odds.append(i)
		else:
			evens.append(i)

	if 2 in evens:
		perms.add(2)
	
	if 3 in odds:
		perms.add(3)

	# Backtracking; only place odd number at the last digit
	# since even numbers are not primes obviously
	for i in range(len(odds)):
		temp = odds.pop(i)
		if temp != 5:
			create_permutations_modified(str(temp))
		else:
			perms.add(5)
		odds.insert(i, temp)
	
	#print('created perms', len(perms))

	# Compute a list of prime numbers up to sqrt(largest permutation)
	# Use Sieve of Eratosthenes 
	largest = 0

	for i in perms:
		if i > largest:
			largest = i
	
	#print('largest among perms', largest)

	# Get primes upto sqrt(largest)
	primes_sieve(int(largest**0.5))
	#print('primes_sieve up to', int(largest**0.5))
	#print('length of up_to', len(up_to))

	for perm in perms:
		if is_prime_modified(perm):
			answer.add(perm)
	
	#print(len(answer))

# Tested with [1,2,3,4,5,6] and [1,2,3,4,5,6,7,8,9]
def create_permutations_regular(curr):
	global perms
	global list_int

	if curr[0] != '0':
		perms.add(int(curr))

	if len(list_int) > 0:
		for i in range(len(list_int)):
			temp = list_int.pop(i)
			create_permutations_regular(str(temp) + curr)
			list_int.insert(i, temp)

def create_permutations_modified(curr):
	global perms
	global evens
	global odds
	global list_int

	if int(curr) % 3 != 0 and curr[0] != '0':
		perms.add(int(curr))

	if len(evens) > 0:
		for i in range(len(evens)):
			temp = evens.pop(i)
			create_permutations_modified(str(temp) + curr)
			evens.insert(i, temp)

	if len(odds) > 0:
		for i in range(len(odds)):
			temp = odds.pop(i)
			create_permutations_modified(str(temp) + curr)
			odds.insert(i, temp)

list_int = [1,2,3,4,5,6,7,8,9,0]
find_primes_modified()
[1,2,3,4,5,6,7,8,9]

