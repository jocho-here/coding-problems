def wiggleSort(nums):
	nums.sort()
	i = 1

	while i < len(nums):
		temp = nums.pop()
		nums.insert(i, temp)
		i += 2
	
nums = [1,2,3,4,5]
wiggleSort(nums)
print nums
