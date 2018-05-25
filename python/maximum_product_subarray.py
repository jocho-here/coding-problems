# Maximum Product Subarray
#
# - Given an integer array nums, find the contiguous subarray within an array
#   (containing at least one number) which has the largest product 
# - Input: [2,3,-2,4]
# - Output: 6 because 3 * 2


# Explanation: Smarter DP.  The algorithm uses the fact that we don't really need consider
#              numbers between the lowest and the highest numbers because whatever comes
#              in between the lowest and the highest numbers, they could be covered by
#              either the lowest one or the highest one.
#              Also, for any combination of the highest and lowest, when multiplied by
#              negative, lowest becomes the next highest and the highest becomes the next
#              lowest while when multiplied by positive, they stay the same.
#              Finally, we have to keep in mind that current entry could be bigger than
#              both the lowest and the highest in case where they are both negative and
#              the current entry is positive.  So we have to track current, 
#              the lowest, and the highest numbers.
#
# Run Time: O(n).  We only track three numbers while iterating over nums.
def sol_unique(nums):
    if len(nums) == 0:
        return 0

    maximum = highest = lowest = nums[0]

    for n in nums[1:]:
        if n > 0:
            highest, lowest = highest * n, lowest * n
        else:
            highest, lowest = lowest * n, highest * n

        if highest < n:
            highest = n
        elif lowest > n:
            lowest = n

        maximum = max(maximum, highest)

    return maximum

# Explanation: It saves multiples in the table for future reference
# Run Time: O(n^2).
def sol_dp(nums):
    table = []

    curr_max = nums[0]

    for i in range(len(nums)):
        temp = [1] * len(nums)
        temp[i] = nums[i]
        table.append(temp)

        if nums[i] > curr_max:
            curr_max = nums[i]

    for i in range(len(nums)):
        for j in range(i):
            table[j][i] = nums[i] * table[j][i-1]

            if curr_max < table[j][i]:
                curr_max = table[j][i]

    return curr_max

# Explanation: Go through entries and include/ exclude current number while maintaining
#              contiguousness and come up with the largest number
# Run Time: O(n^2).  The outer index increases from 0 to len(nums).  Everytime it
#           recursively calls itself, it multiplies new entry to the previous result
#           while starting a fresh new recursive call from current entry.  We memoize 
#           the previous result to improve the runtime from O(n^3) to O(n^2).
# Note: It takes more time for recursive algorithm than brute-force
def sol_recur(nums):
    if len(nums) == 0:
        return 0

    return sol_recur_helper(nums, 1, nums[0])

def sol_recur_helper(nums, i, result):
    if i == len(nums):
        return result

    in_curr = sol_recur_helper(nums, i+1, result * nums[i])
    ex_curr = sol_recur_helper(nums, i+1, nums[i])

    return max(result, in_curr, ex_curr)

# Explanation: Go through every possible subarrays and find the largest one
# Run Time: O(n^3).  The outer index increases from 0 to len(nums), the mid index
#           increases from the outer index to len(nums), and the inner index multiplies
#           continguous subarray numbers in O(n)
# Improvement: We can use memoization to make the run time from O(n^3) to O(n^2) by 
#              memorizing the previous multiplication
def sol_brute(nums):
    if len(nums) == 0:
        return 0

    curr_max = nums[0]
    
    for i in range(len(nums)): # outer index
        curr_mult = 1
        for j in range(i, len(nums)): # inner index
            curr_mult *= nums[j]

            if curr_mult > curr_max:
                curr_max = curr_mult

    return curr_max

nums = [-1,-4,4,-4,-5,-2,-1,-1,2,3,5,1,3,-6,-1,-1,-2,-1,-4,4,-4,-5,-2,-1,-1,2,3,5,1,3,-6,-1,-1,-2,-1,-4,4,-4,-5,-2,-1,-1,2,3,5,1,3,-6,-1,-1,-2,-1,-4,4,-4,-5,-2,-1,-1,2,3,5,1,3,-6,-1,-1,-2]
#print(sol_recur(nums))
#print(sol_brute(nums))
#print(sol_unique(nums))
#print(sol_dp(nums))
