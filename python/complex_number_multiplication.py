def complexNumberMultiply(a, b):
	# In the form of a+bi
	# -100 <= a, b <= 100
	# a, b:  str
	# rtype: str
	# example: Input: "1+1i", "1+1i"
	#          Output: "0+2i"
	a_split = a.split('+')
	b_split = b.split('+')

	a_real = int(a_split[0])
	a_imaginery = int(a_split[1][:len(a_split[1]) - 1])
	b_real = int(b_split[0])
	b_imaginery = int(b_split[1][:len(b_split[1]) - 1])

	real_part = (a_real * b_real) - (a_imaginery * b_imaginery)
	imaginery_part = a_imaginery * b_real + b_imaginery * a_real
	
	return str(real_part) + '+' + str(imaginery_part) + 'i'

print complexNumberMultiply('1+-1i', '1+-1i')
