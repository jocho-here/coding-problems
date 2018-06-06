# Maximal Rectangle
# - Given a 2-d list, come up with the size of the largest rectangle
#   that is only consisted of 1's

# Explanation: The algorithm looks at the matrix in the similar way as the recursive
#              algorithm does but it builds up the cumulative matrix as it goes.
#              Since the cumulative numbers are built from right to left, we want to
#              start from the bottom right and build our way up to the top left so
#              we could use memoization to make our running time faster.
#              While we are building the cumulative matrix, as previously, we are going
#              to calculate the maximum rectangle as we go with the same algorithm as
#              the recursive algorithm.
def sol_dp(matrix):
    return "Need to work on this"

# Helper function
def change_to_cumulative(rect):
    new_rect = []

    for r in range(len(rect)):
        new_r = []
        cumul = 0

        for c in range(len(rect[r])-1, -1, -1):
            curr = int(rect[r][c])

            if curr == 1:
                cumul += curr
            else:
                cumul = 0
            new_r.insert(0, cumul)

        new_rect.append(new_r)

    return new_rect

# Explanation: The algorithm first changes the given matrix into a what's called
#              cumulative matrix.  At every point, the value shows you how many
#              reachable 1's are there cumulatively (change_to_cumulative()).
#              If we think the size of matrix is equal to n, then this transformation
#              takes O(n) running time.
#              Next, with the new matrix, we now iterate through the whole matrix
#              from the top-left corner to the bottom right corner.  At every point,
#              the algorithm calculates its biggest rectangle possigle by looking at
#              the cumulative numbers and update the possible maximum it iterates
#              down.  At each row, we compare the current minimum cumulative number
#              with the current cumulative number and see if we face a smaller number.
#              When the current cumulative number is smaller, than that means as we
#              go deeper down, we will only be able to count as many 1's as that
#              smallest cumulative number much.  So we have to keep in track of
#              current rectangle is biggest as we go down the rows.
# Run Time: O(n^2).  We have O(n) from the change_to_cumulative(), O(n) for the 
#           inner loop that goes deeper down, and the O(n) for the outer loop that
#           loops through the whole rectangle, which together become O(n^2).
def sol_bruteforce(matrix):
    new_rect = change_to_cumulative(matrix)
    rtn_val = 0

    for rr in range(len(new_rect)):
        for c in range(len(new_rect[rr])):
            min_cul = new_rect[rr][c]
            curr_max = new_rect[rr][c]

            for r in range(rr, len(new_rect)):
                if new_rect[r][c] == 0:
                    break
                else:
                    if new_rect[r][c] < min_cul:
                        min_cul = new_rect[r][c]
                    curr_max = max((r-rr+1)*min_cul, curr_max)
            rtn_val = max(curr_max, rtn_val)
    return rtn_val


rect = [
           ["1","1","1","0","0"],
           ["1","1","1","1","1"],
           ["1","1","1","0","1"],
           ["1","0","0","1","0"]
       ]
print(sol_rec(rect))
