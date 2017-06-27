def depth_sum(nested_list):
	return rec_depth_sum(nested_list, 1)

def rec_depth_sum(nested_list, depth):
	sum = 0
        
	for comp in nested_list:
		if isinstance(comp, list):
			sum += rec_depth_sum(comp, depth + 1)
		else:
			sum += depth * comp
        
	return sum

print str(depth_sum([1,[4,[6]]]))
