def wiggleSort(nums):
	bigger = True
	i = 1

	while i < len(nums):
		if (bigger and (not nums[i - 1] <= nums[i])) or (not bigger and (not nums[i - 1] >= nums[i])):
			temp = nums[i]
			nums[i] = nums[i - 1]
			nums[i - 1] = temp
		else:
			i += 1
			bigger = not bigger

nums = [1,2,3]
wiggleSort(nums)
