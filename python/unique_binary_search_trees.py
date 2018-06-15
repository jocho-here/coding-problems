# Unique Binary Search Trees
# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n ?

# Explanation: We could use dictionary to save some look up time since many of recursive calls
#              hit the same n numbers
# Run Time: O(n log(n)) since we don't repeat anything that has been already explored but still
#           go for log(n) depth to calculate answers up to n
def sol_dp(n):
    if n < 3:
        return n

    ds = [1] * (n + 1)

    for i in range(2, n + 1):
        depth = int((i + 1) / 2)
        sol = 0

        for j in range(0, depth - 1):
            sol += 2 * ds[j] * ds[i - j - 1]

        if i % 2:
            sol += ds[depth - 1] ** 2
        else:
            sol += 2 * ds[depth] * ds[i - depth - 1]

        ds[i] = sol

    return ds[n]

# Explanation: The trick here is that we have to calculate the number of different numerical
#              calculation we have to come up for getting the final answer.
#              For example:
#              <1> -> 1                             = 1
#              <2> -> 1       2       1        2
#                      \     /    =    \      /     = 1 x 2 = 2
#                       2   1          <1>  <1>
#              <3> -> 1        3     2
#                      \      /     / \             = 2 x 2 + 1 x 1 = 5
#                      <2>  <2>   <1> <1>
#              <4> -> 1        4     2        3
#                      \      /     / \      / \    = 5 x 2 + 1 x 2 x 2 = 14
#                      <3>  <3>   <1> <2>  <2> <1>
#              ...
#              There is a pattern: to get the total number of possible BST, we have to go
#              int((n + 1) / 2) deeper from n to get the answer.  For example, for n = 3,
#              we have to check int((3 + 1) / 2) = 2 deeper from n, which 2 & 1.  Therefore,
#              as recursive solution, it should call sol_rec() function int((n + 1) / 2) times.
# Run Time: O(log(n)^n).  For each n, to n-1, n-2, ..., 1 recursively to calculate one type of tress
#           with the certain root.  We have to do this for round_up(n / 2), so it's O(log(n)^n)
def sol_rec(n):
    if n == 1 or n == 0:
        return 1

    depth = int((n + 1) / 2)
    rtn_val = 0

    for i in range(0, depth - 1):
        rtn_val += 2 * sol_rec(i) * sol_rec(n - i - 1)

    # odd
    if n % 2:
        rtn_val += sol_rec(depth - 1) ** 2
    else:
        rtn_val += 2 * sol_rec(depth) * sol_rec(n - depth - 1)

    return rtn_val

print('sol_dp')
for i in range(2, 7):
    print(i, sol_dp(i))

print('sol_rec')
for i in range(2, 7):
    print(i, sol_rec(i))
