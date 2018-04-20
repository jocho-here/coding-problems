# Longest increasing subsequence

int_list = [3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6]

# Backtracking method
# O(2^n)
def process_backtracking(i, tot, prev):
	if i == len(int_list):
		return tot

	
	if int_list[i] > prev:
		a = process_backtracking(i+1, tot+1, int_list[i])
		b = process_backtracking(i+1, tot, prev)

		return max(a,b)
	else:
		return process_backtracking(i+1, tot, prev)

# Dynamic programming method
# O(n^2)
def process_dp():
	dp_list = [-99999] + int_list

	ds = []

	for i in range(len(dp_list)):
		ds.append([0] * (len(dp_list) + 1))
	
	for j in range(len(dp_list) - 1, 0, -1):
		for i in range(0, j):
			if dp_list[i] >= dp_list[j]:
				ds[i][j] = ds[i][j+1]
			else:
				ds[i][j] = max(ds[i][j+1], 1 + ds[j][j+1])

			print(dp_list)
			print('dp_list[i]:' + str(dp_list[i]) + ', dp_list[j]: ' + str(dp_list[j]))
			for k in ds:
				print(k)
			print('')
			a = raw_input('')
	
	return ds[0][1]

	

print(process_backtracking(0, 0, -1))
print(process_dp())
