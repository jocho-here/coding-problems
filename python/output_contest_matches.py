def find_contest_match(n):
	rep = n.bit_length() - 1
	container = rep % 2
	tuple_container = []
	tuple_container.append([])
	tuple_container.append([])

	for x in xrange(1, (n/2) + 1):
		curr_str = '(' + str(x) + ',' + str(n - x + 1) + ')'
		tuple_container[container].append(curr_str)
	
	while rep > 1:
		rep = rep - 1
		next_container = rep % 2
		tuple_container[next_container] = []

		for x in xrange(0, (len(tuple_container[container]) / 2)):
			curr_str = '(' + tuple_container[container][x] + ','+\
				tuple_container[container][len(tuple_container[container]) - x - 1] + ')'
			tuple_container[next_container].append(curr_str)

		container = next_container
	
	print tuple_container[container][0]

# change this number!
find_contest_match(16)
