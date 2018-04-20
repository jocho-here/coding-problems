A = [0, 3, 4, 7]
B = [1, 5, 8]
ds = {0:[1],1:[2],2:[0,3],3:[4],4:[5,6],5:[6,7],6:[3],7:[8],8:[9],9:[7]}
visited = {}
status = {}
L = []

def find_reachablesDFS(start):
	global L
	global visited
	stack = [start]

	for i in range(10):
		visited[i] = False

	while len(stack) > 0:
		curr = stack.pop()

		visited[curr] = True
		L.append(curr)

		for i in ds[curr]:
			if visited[i] == False:
				stack.append(i)
# My solution
def find_ABunfairDFS():
	global visited
	nodes_to_check = []

	for i in A:
		if i in L:
			nodes_to_check.append(i)
	
	for i in range(10):
		visited[i] = False

	for i in nodes_to_check:
		stack = [i]

		for j in visited:
			visited[j] = False

		while len(stack) > 0:
			curr = stack.pop()

			visited[curr] = True

			for j in ds[curr]:
				if visited[j] == True:
					return True
				elif j not in B:
					stack.append(j)

	return False

# Jeff's notes solution
def is_acyclicDFS(v):
	global status
	global ds

	status[v] = 'Active'

	for w in ds[v]:
		if w not in B:
			if status[w] == 'Active':
				return False
			elif status[w] == 'New':
				if is_acyclicDFS(w) == False:
					return False
	
	status[v] = 'Finished'

	return True

def is_acyclic():
	global status
	nodes_to_check = []

	for i in A:
		if i in L:
			nodes_to_check.append(i)
	
	for i in range(10):
		status[i] = 'New'
	
	for i in nodes_to_check:
		if status[i] == 'New':
			if is_acyclicDFS(i) == False:
				return False
	
	return True


if __name__ == "__main__":
	find_reachablesDFS(0)
	print("Reachables by 0")
	print(L)

	print("Is this (A-B)unfair?")
	print(find_ABunfairDFS())
	print(is_acyclic())
