def hammingDistance(x, y):
	if x < y:
		bigger = y

	else:
		bigger = x
	
	z = x ^ y
	rtn_val = 0

	while z > 0:
		if z & 1:
			rtn_val += 1

		z = z >> 1
	
	return rtn_val

print hammingDistance(0b0001, 0b0100)
