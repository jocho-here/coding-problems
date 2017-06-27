def findComplement(num):
	"""
	:type num: int
	:rtype: int
	"""
	n = 1 
	while n <= num:
		n = n << 1
	n -= 1

	return n ^ num

print findComplement(1)
