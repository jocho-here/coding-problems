words = ['my','name','is','joseph','hi']
input_str = ''

def is_word(i, j):
	if input_str[i: j+1] in words:
		return True
	
	return False

# back tracking method
# run time O(2^n) - exponential
def splittable_backtracking(i):
	if i == len(input_str):
		return True

	for j in range(i, len(input_str)):
		if is_word(i, j):
			if splittable_backtracking(j+1):
				return True
	
	return False

# dynamic programming method
# run time O(n^2) - quadratic
def splittable_dp():
	can_split = [False] * len(input_str)
	can_split.append(True)
	
	for i in range(len(input_str) - 1, -1, -1):
		for j in range(i, len(input_str)):
			if is_word(i,j) and can_split[j+1] == True:
				can_split[i] = True
	
	return can_split[0]
	

import sys

if len(sys.argv) != 2:
	print("usage: python string_split.py <input_string>")
else:
	# back tracking method
	#input_str = str(sys.argv[1])
	#print(splittable_backtracking(0))

	# dynammic programing method
	input_str = str(sys.argv[1])
	print(splittable_dp())
