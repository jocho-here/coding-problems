# Explanation: As we've explored in recursive algorithm, we have three choices to make: insert, delete,
#              and either replace or leave it as it is.  At every point, we only want to look at the 
#              operations up to next character plus the minimum of the three choices upon the current
#              character.  Such recurrence eventually look at a certain character repeatedly because
#              numerous recursive calls would be looking at the same point again and again.  We also
#              realize that at every point, we need to consider three dependencies, which are:
#                 - (i, j+1) + 1
#                 - (j+1, i) + 1
#                 - (i+1, j+1) + (word1[i] != word2[j])
#              Through memoizing those "future" point operations in two-dimensional data structure, we
#              could save running time.
#              The base cases are when we are at i or j and we disregard no-op characters and just count
#              all operations needed from that certain i or j to the last character.
# Run Time: O(n * m) since we are filling up a two-dimensional data structure of the size (n * m).
def min_distance_dp(word1, word2):
    edit_d = []

    for i in range(len(word1)):
        temp = [0] * len(word2) + [i+1]
        edit_d.insert(0, temp)

    temp = []
    for j in range(len(word2) + 1):
        temp.insert(0, j)

    edit_d.append(temp)

    for i in range(len(word2) - 1, -1, -1):
        for j in range(len(word1) - 1, -1, -1):
            edit_d[j][i] = min(edit_d[j][i+1] + 1, \
                               edit_d[j+1][i] + 1, \
                               edit_d[j+1][i+1] + (word1[j] != word2[i]))

    return edit_d[0][0]
    
    
# Explanation: We have 4 options: insert, delete, and replace, if not maching, or leave the current
#              character if matching.  Our recursive solution will try to explore all the possibilities
#              and come up with the optimum solution of them all.  The algorithm will compare
#              the number of operations needed for when inserting, deleting, replacing, or leaving
#              the current goal's char.  For every option, the algorithm calls the function recursively
#              and look at the next step to take.
#              Base case is when the index hits the length of word2 or length of word1
# Run Time: O(n^3) is the upper limit when we consider replacing everytime and O(n^2) is the lower
#           limit when we don't at all
# Improvement: We realize that our string manipulation to make new word1 takes quite a lot of time and
#              also unnecessary because we don't really need to track what we've added or deleted since
#              if we keep two indices and move as accordingly, for addition, we could say we've added 
#              the current word2's char to word1 and therefore, we can increment word2's index and move on
#              to the next char of word2.  For the deletion, we could say we've deleted current word1's
#              char, therefore increment word1's index while keeping word2's index as it is.
#              The base case is when we either hit the len(word1) with i or len(word2) with j.  In that
#              case, we should return the left-overs; if i == len(word1), then we should return how many
#              steps are further needed to add to word1 so it matches with word2; if j == len(word2), then
#              we should return how many steps are further needed to delete chars in word1 so it matches 
#              with word2 since the word2 indes has reached the end of it.
def min_distance_recur(word1, word2):
    return min_distance_recur_smart_helper1(0, 0, word1, word2)
    #return min_distance_recur_helper(0, 0, word1, word2)
    
# Smarter way, mimicing CS 374 algorithm.  The original version was counter-intuitive so
# I made it to go bottom up
def min_distance_recur_smart_helper(i, j, word1, word2):
    if i == len(word1):
        return len(word2) - j
    elif j == len(word2):
        return len(word1) - i

    a = min_distance_recur_smart_helper(i, j+1, word1, word2) + 1 # insertion
    b = min_distance_recur_smart_helper(i+1, j, word1, word2) + 1 # deletion
    c = min_distance_recur_smart_helper(i+1, j+1, word1, word2) + (word1[i] != word2[j])

    return min(a,b,c)

# Very intuitive recursive function
def min_distance_recur_helper(i, count, word1, word2):
    if i == len(word2) or i == len(word1):
        return count + abs(len(word1) - len(word2))

    insert = min_distance_recur_helper(i+1, count+1, word1[:i] + word2[i] + word1[i:], word2)
    delete = min_distance_recur_helper(i, count+1, word1[:i] + word1[i+1:], word2)
    
    if word1[i] == word2[i]:
        replace = min_distance_recur_helper(i+1, count, word1, word2)
    else:
        replace = min_distance_recur_helper(i+1, count+1, word1[:i] + word2[i] + word1[i+1:], word2)

    return min(insert, delete, replace)
    
#print(min_distance_recur('horse', 'ros'))
#print(min_distance_recur('prosperity', 'properties')) # time limit exceeded on leetcode
print(min_distance_dp('horse', 'ros'))
print(min_distance_dp('interaction', 'execution'))
print(min_distance_dp('prosperity', 'properties'))
