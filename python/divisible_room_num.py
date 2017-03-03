def num_divisible_room(x, y, n, m):
	# x, y are the dividing factors
	# n is total number of floors in the building
	# m_k is number of rooms on floor k
	room_nums = []

	for floor in range(0, n):
		for room in range(0, int(m[floor])):
			room_nums.append((floor + 1) * 100 + (room + 1))
	
	counter = 0

	for room_num in room_nums:
		if room_num % x == 0 or room_num % y == 0:
			counter += 1
	
	return counter

import sys, string

if len(sys.argv) == 2:
	try:
		f = open(sys.argv[1], 'r')
	except IOError:
		print("usage: python divisible_room_num.py [input_file_name]")
		sys.exit(1)
	
	c = int(f.readline())
	outputs = []

	for i in range(0, c):
		n = f.readline();

		while n == '\n':
			n = f.readline()

		n = int(n)
		m = string.split(f.readline())
		temp = string.split(f.readline())
		x = int(temp[0])
		y = int(temp[1])
		outputs.append("Case #" + str(i + 1) + ": " + str(num_divisible_room(x, y, n, m)))
		f.readline()

	for output in outputs:
		print(output)

	f.close()
elif len(sys.argv) == 1:
	c = int(raw_input())
	print('')
	outputs = []

	for i in range(0, c):
		n = int(raw_input())
		m = string.split(raw_input())
		temp = string.split(raw_input())
		x = int(temp[0])
		y = int(temp[1])
		outputs.append("Case #" + str(i + 1) + ": " + str(num_divisible_room(x, y, n, m)))

	for output in outputs:
		print(output)
else:
	print("usage: python divisible_room_num.py [input_file_name]")
