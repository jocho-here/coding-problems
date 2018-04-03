ds = {0:0, 1:1}

# back tracking method
# run time O(2^n) - exponential
def fibonacci_recursive(i):
	if i == 0:
		return 0
	elif i == 1:
		return 1
	else:
		return fibonacci_recursive(i-1) + fibonacci_recursive(i-2)

# dynamic programming method
# run time O(n)
def fibonacci_dp(i):
	if i in ds:
		return ds[i]
	else:
		return fibonacci_dp(i-1) + fibonacci_dp(i-2)

# run time O(n) much faster linear
def fibonacci_dp_alt(i):
	if i == 0:
		return 0
	elif i == 1:
		return 1

	prev = 0
	curr = 1

	for j in range(i - 1):
		temp = curr
		curr = prev + curr
		prev = temp
	
	return curr

import sys

if len(sys.argv) != 2:
	print("usage: python string_split.py <input_int>")
else:
	print(fibonacci_dp_alt(int(sys.argv[1])))
	print(fibonacci_dp(int(sys.argv[1])))
	print(fibonacci_recursive(int(sys.argv[1])))
