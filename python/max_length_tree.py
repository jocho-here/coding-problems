tree = {}
labels = []
node_l_depth = {}
max_len = 0

def solution(A, E):
	global labels
	global tree

	labels = A

	# Building a tree
	for i in range(int(len(E) / 2)):
		if E[i*2] in tree:
			tree[E[i*2]].append(E[i*2 + 1])
		else:
			tree[E[i*2]] = [E[i*2 + 1]]
	
	get_each_node_l_depth(E[0])
	
	return max_len

def get_each_node_l_depth(i):
	global labels
	global node_l_depth
	global tree
	global max_len

	node_l_depth[i] = 0
	curr_len = 0

	if i in tree:
		for child in tree[i]:
			get_each_node_l_depth(child)

			if labels[i-1] == labels[child-1]:
				curr_len += node_l_depth[child] + 1

				if node_l_depth[child] + 1 > node_l_depth[i]:
					node_l_depth[i] = node_l_depth[child] + 1
	
	if curr_len > max_len:
		max_len = curr_len

A = [1,1,1,2,2]
E = [1,2,1,3,2,4,2,5]

print(solution(A,E))
