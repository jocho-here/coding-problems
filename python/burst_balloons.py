# Explanation: Recursive algorithm is all about comparing all the possible options and
#              coming up with the optimal solution of what's looked after.  Usually,
#              when an algorithm does not need to select all items in a given list,
#              it either chooses ith item or pass it and go to (i+1)th item and compare
#              the result to get the optimal solution.  This algorithm is asking to
#              include all items in some order that will result in the maximum sum.
#              This is rather looking for the optimal permutation of choices between
#              nums.  So at every level of the recursion tree, the algorithm chooses 
#              one item from nums and recursively call with one-less sized nums.  Then
#              it recursively calls the function with further one-less sized nums by
#              iterating through nums and popping one.  At every level, it compares 
#              with popping another item and returns the maximum sum.
# Run Time: O(n!) since it's going through all the permutations
# Note: Time limit exceeded on [35,16,83,87,84,59,48,41,20,54]
def sol_rec(nums):
    if len(nums) == 1:
        return nums[0]
    
    curr_max = 0

    for c in range(len(nums)):
        if c == 0:
            curr_val = sol_rec(nums[1:]) + nums[0]*nums[1]
        elif c == len(nums) - 1:
            curr_val = sol_rec(nums[:c]) + nums[c]*nums[c-1]
        else:
            curr_val = sol_rec(nums[:c] + nums[c+1:]) + nums[c-1]*nums[c]*nums[c+1]

        if curr_val > curr_max:
            curr_max = curr_val

    return curr_max

# Explanation: Subproblem is to find the max sum when nums have certain items at
#              the certain point.  Then we could memoize these values and go up to the
#              previous level (in terms of number of items in nums) to use the
#              memoized values for faster calculation.
#              For example, if we start out with [3,1,5,8], then we have two paths
#              that will give us [3,1] after popping two; 1) Pop 8 -> 5, 2) Pop 5 -> 8.
#              By saving the maximum popping sum for [3,1], we could use it multiple
#              time by referencing it.
# Run Time: O(C(n, k) * k for k from 1 to n) since we have C(n,k) cases for each level 
#           and k comparisons to make for a permutation with 'k' numbers
# Note: Time limit exceeded on [2,4,8,4,0,7,8,9,1,2,4,7,1,7,3,6]
def sol_mem(nums, ds):
    if len(nums) == 1:
        return nums[0]

    if str(nums) in ds:
        return ds[str(nums)]
    
    curr_max = 0

    for c in range(len(nums)):
        if c == 0:
            curr_val = sol_mem(nums[1:], ds) + nums[0]*nums[1]
        elif c == len(nums) - 1:
            curr_val = sol_mem(nums[:c], ds) + nums[c]*nums[c-1]
        else:
            curr_val = sol_mem(nums[:c] + nums[c+1:], ds) + nums[c-1]*nums[c]*nums[c+1]

        if curr_val > curr_max:
            curr_max = curr_val

    ds[str(nums)] = curr_max

    return curr_max

# Explanation: It looks at the last index to pop and uses bottom-up algorithm
#              (tabulation).  It fills up the table in terms of:
#                1) what numbers are we considering to have in the list RIGHT NOW?
#                2) which number are we considering to pop the last?
#              With such considerations in mind, we could first start out with the
#              length 1 lists while accepting the environment to be the whole list.
#              Then, we go for length 2 lists.  We then iterate through the contents of
#              each list, and consider each number to be popped the last.  Then we
#              compare them to get the optimal, and save it in the table.  It memorizes
#              what's the best solution for n large list (in the given list) with 
#              certain items in it by comparing different options for last popped.
# Run Time: O(n^3) since we fill up the n^2 table and while doing that, we consider
#           n different choices for each.
# Note: 1) https://www.youtube.com/watch?v=IFNibRVgFBo
#       2) https://www.geeksforgeeks.org/tabulation-vs-memoizatation/
def sol_dp(nums):
    nums = [1] + nums + [1]
    n = len(nums)
    ds = []

    for i in range(n):
        ds.append([0] * n)

    for i in range(n - 2):
        ds[i + 1][i + 1] = nums[i]*nums[i + 1]*nums[i+2]

    for size in range(2, n-1):       # considering lists of different sizes
        for i in range(1, n-size):   # iterating through the list with the given size
            curr_max = 0

            for j in range(i, i + size): # last balloon index
                curr_max = max(curr_max, ds[i][j-1] + ds[j+1][i+size-1] \
                           + nums[i-1]*nums[j]*nums[i+size])

            ds[i][i+size-1] = curr_max

    return ds[1][n-2]

nums = [2,4,8,4,0,7,8,9,1,2,4,7,1,7,3,6]
#print(sol_rec(nums))
print(sol_mem(nums, {}))
#print(sol_dp(nums))
