def quicksort(unsorted_list, l_i, h_i):
	# Basecase is when l_i is equal to (or larger than) h_i
	if l_i < h_i:
		i = l_i - 1
		pivot = unsorted_list[h_i]

		# When it's time to swap, i will always be pointing at larger one
		# while j will be pointing at smaller one
		# Example
		# 4, 3, 5, 1, [2]
		# ij4, 3, 5, 1, [2]
		# i4, j3, 5, 1, [2]
		# i4, 3, j5, 1, [2]
		# i4, 3, 5, j1, [2]  =>  i1, 3, 5, j4, [2]
		for j in xrange(l_i, h_i):
			if unsorted_list[j] <= pivot:
				i = i + 1
				unsorted_list[i], unsorted_list[j] =\
					unsorted_list[j], unsorted_list[i]

		# i1, 3, 5, j4, [2]  =>  i1, [2], 3, 5, 4
		unsorted_list[i + 1], unsorted_list[h_i] =\
			unsorted_list[h_i], unsorted_list[i + 1]
		
		pi = i + 1
		quicksort(unsorted_list, l_i, pi - 1) # [1,] 2, 3, 5, 4
		quicksort(unsorted_list, pi + 1, h_i) # 1, 2, [3, 5, 4]

import sys
# Increasing recursion limit
sys.setrecursionlimit(100000)

unsorted_list = []
for x in xrange(10000, -1, -1):
	unsorted_list.append(x)

quicksort(unsorted_list, 0, len(unsorted_list) - 1)
#print unsorted_list
