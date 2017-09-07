def quickSort(arr,low,high):
	if low < high:
		i = low - 1
		pivot = arr[high]

		for j in range(low, high):
			if arr[j] <= pivot:
				i = i + 1
				arr[i], arr[j] = arr[j], arr[i]

		arr[i + 1], arr[high] = arr[high], arr[i + 1]
		
		pi = i + 1
		quickSort(arr, low, pi-1)
		quickSort(arr, pi+1, high)

import sys
sys.setrecursionlimit(100000)

unsorted_list = []

for x in xrange(10000, -1, -1):
	unsorted_list.append(x)

quickSort(unsorted_list, 0, len(unsorted_list) - 1)
#print unsorted_list
