def matrixReshape(nums, r, c):
	if r * c != len(nums) * len(nums[0]):
		return nums
	
	rtn_val = []
	i = 0
	new_num = []

	for comp in nums:
		for num in comp:
			new_num.append(num)
			i += 1

			if i == c:
				i = 0
				rtn_val.append(new_num)
				new_num = []
	
	return rtn_val
	
print(matrixReshape([[1,2],[3,4]], 1, 4))
