import sys

input_1 = ''
input_2 = ''
ds = None

# Example: AL[G][O]R[ ]I[ ]T[H][M]   ==>  6
#          AL T    R U I S T I  C
#
# Recursive algorithm
#
# Running time is roughly between O(2^n) and O(3^n)
#
# Calculate all the possibilities and get the minimum
# 1. Basecase is when either i or j is 0, then we just return as much as we have left
#    with the other word
# 2. Otherwise compare...:
# 	a) When we add input_1[i] character to input_2        (insertion)
#	b) When we delete input_2[j] from input_2             (deletion)
#	c) When we count 'i'th and 'j'th, both, characters    (substitution)
#		- If input_1[i] == input_2[j]       >>>   No change so don't count
#		- Else if input_1[i] != input_2[j]  >>>   Substitution so add 1
def edit_distance_recursive(i, j):
	if i == 0:
		return j
	elif j == 0:
		return i
	
	a = edit_distance_recursive(i - 1, j) + 1    # +1 for insertion
	b = edit_distance_recursive(i, j - 1) + 1    # +1 for deletion
	c = edit_distance_recursive(i - 1, j - 1) \
	           + (input_1[i-1] != input_2[j-1])  # possible +1 for substitution
	
	return min(a,b,c)

# DP algorithm
#
# Running time is O(nm)
#
# Decrease running time y memoization over dependencies ([i-1,j], [i,j-1], [i-1,j-1])
#

def edit_distance_dp(i, j):
	ds = [range(len(input_2)+1)]

	for i in range(1, len(input_1)+1):
		temp = [i] + [0]*(len(input_2))
		ds.append(temp)
	
	for i in range(1, len(input_1)+1):
		#ds[i][0] = i

		for j in range(1, len(input_2)+1):
			if input_1[i-1] == input_2[j-1]:
				ds[i][j] = min(ds[i-1][j]+1,ds[i][j-1]+1,ds[i-1][j-1])
			else:
				ds[i][j] = min(ds[i-1][j],ds[i][j-1],ds[i-1][j-1]) + 1

			print('i: ' + str(i-1) + ',j: ' + str(j-1))

			for k in ds:
				print(k)
			print('')
			a = raw_input('')

	return ds[len(input_1)][len(input_2)]

if len(sys.argv) != 3:
	print("usage: python edit_distance.py <input_string_1> <iput_string_2>")
else:
	input_1 = sys.argv[1]
	input_2 = sys.argv[2]

	#print(edit_distance_recursive(len(input_1), len(input_2)))
	print(edit_distance_dp(input_1, input_2))
