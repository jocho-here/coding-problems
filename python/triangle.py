# Explanation: As discussed in recursive solution, every node has two children.
#              Since (r,c) needs cumulative min sums for (r+1,c) and (r+1,c+1), we
#              could use memoization to save previously calculated mins at every
#              row to our data structure and move up a row and calculate the samething
#              again.
# Run Time: O(n) since it goes through every node once
def sol_dp(triangle):
    t = triangle
    ds = t[-1]

    for r in range(len(t)-2,-1,-1):
        for c in range(len(t[r])):
            ds[c] = min(ds[c] + t[r][c], ds[c+1] + t[r][c])

    return ds[0]

# Explanation: As always, recursive function tries every possible options.  In this
#              case, the algorithm is basically doing DFS of the whole triangle where
#              two children of, (row,column), (i,j) are (i+1,j) and (i+1,j+1), except
#              for the last row.  Then, we just need to find the minimum of sums.
# Run Time: O(2^n) since every node has two branches and there are O(n) nodes
def sol_rec(t,r,c):
    if not r < len(t):
        return 0
    
    return t[r][c] + min(sol_rec(t,r+1,c),sol_rec(t,r+1,c+1))

triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

print(sol_rec(triangle,0,0))
