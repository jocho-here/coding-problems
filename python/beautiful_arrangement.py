def countArrangement(N):
	available_dict = {}

	for i in xrange(1, N + 1):
		curr_available = []

		for t in xrange(1, N + 1):
			if i % t == 0 or t % i == 0:
				curr_available.append(t)
		
		available_list.setdefault(i, curr_available)
	
	
	# 4 * 3 * 2 * 1 / 3*2*1 * 1
	# N == 4
	# 1,2,3,4
	# 1,4,3,2
	# 2,1,3,4
	# 2,4,3,1
	# 3,2,1,4
	# 3,4,1,2
	# 4,2,3,1
	# 4,1,3,2
	# 1- 1,2,3,4
	# 2- 1,2,4
	# 3- 1,3
	# 4- 1,2,4
