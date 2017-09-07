def insertionsort(unsorted_list):
	# Loop through all the entries
	for i in xrange(0, len(unsorted_list)):
		j = i

		# Lower the index of current entry while seeing larger entries
		while j > 0 and unsorted_list[j - 1] > unsorted_list[j]:
			unsorted_list[j - 1], unsorted_list[j] = unsorted_list[j], unsorted_list[j - 1]
			j -= 1

a = []
for x in xrange(1000, 0, -1):
	a.append(x)

insertionsort(a)
print a
