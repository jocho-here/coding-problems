# Unique Paths
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the
# diagram below).  The robot can only move either down ro right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).  How many possible unique paths are there?

# Explanation: The sub-problem was to find how many paths are there to get from (1,1)
#              to (i,j).  This (i,j) are not just the destination coordinate but also
#              for every squares possible.  For example, on a grid with m = 4 and
#              n = 3, to find out how many paths are there to get from (1,1) to (4,3),
#              we first have to know how many paths are there to get from (1,1) to
#              (3,3) and (4,2), and so on.  If we know how many paths are there to 
#              get to (i-1,j) and (i,j-1), then we could add them together to come up
#              with the answer for (i,j)
# Run Time: O(mn)
def sol_dp(m, n):
    ds = [[1] * n]

    for i in range(1, m):
        curr_d = [1]
        
        for j in range(1, n):
            curr_d.append(curr_d[j-1] + ds[i-1][j])

        ds.append(curr_d)

    return ds[m-1][n-1]

# Explanation: Try out all the possible solutions and collect all the possible steps
#              by stepping right or down and recursively calling the function.  The
#              basecase would be when curr_i and curr_j hit the destination or when 
#              either curr_i or curr_j exceed the grid limits.
# Run Time: 2^(m+n)
def sol_rec(m, n, curr_i, curr_j):
    if curr_i == m and curr_j == n:
        return 1
    elif curr_i > m or curr_j > n:
        return 0

    return sol_rec(m,n,curr_i+1,curr_j) + sol_rec(m,n,curr_i,curr_j+1)

m = 23
n = 12

#print(sol_rec(m,n,1,1))
print(sol_dp(m,n))
