# Perfect Squares
# Given a positive integer n, find the least number of perfect square numbers
# (for example 1, 4, 9, 16, ...) which sum to n

# Explanation: Sub-problem of recursive algorithm is what's the least number of
#              perfect square numbers to (n - curr_sqr**2).  Then we could just
#              find the min of (n - curr_sqr**2) + 1, +1 for curr_sqr**2, and return.
# Run Time: O(n * log(n)).  We have to calculate all the answers up to n.  At every 
#           i for i = 1 to n, out calculation expand at most log(n).
def sol_dp(n):
    if n < 4:
        return n

    ds = [0] * (n+1)
    ds[0] = 0
    ds[1] = 1
    
    for i in range(2, n + 1):
        curr_min = ds[i - 1] + 1
        curr_sqr = 2

        while curr_sqr**2 <= i:
            curr_sol = ds[i - curr_sqr**2] + 1

            if curr_sol < curr_min:
                curr_min = curr_sol
            curr_sqr += 1

        ds[i] = curr_min

    return ds[n]

# Explanation: This problem is about finding 1) division of n 2) finding the
#              least size among answers to 1).  For finding division, recursive
#              answer will be going through all the possible options.
# Run Time: O(log(n)^n).  For every level, we have log(n) options to loop through.
#           Then this goes on for n times in depth so it is O(log(n)^n)
def sol_rec(n, depth):
    if n == 0:
        return depth

    rtn_val = 9999
    curr_sqr = 1

    while curr_sqr <= n:
        curr_rtn = sol_rec(n - curr_sqr**2, depth + 1) 
        rtn_val = min(curr_rtn, rtn_val)

        curr_sqr += 1

    return rtn_val

for i in range(50):
    if sol_rec(i, 0) != sol_dp(i):
        print(i)
        break
    else:
        print('passed {}'.format(i))
