# Longest Palindromic Substring
#  - Given a string 's', find the longest palindromic substring in 's'.  You may assume that the maximum length of 's' is 1000.

# Explanation: It goes from left to right and checks the longest target substring using
#              the brute-force algorithm.
# Run time: O(n^2).  The outer index increases over 's' and the inner index increases from current outer index to as far as it
#           reach while maintaining palindromic substring
def longest_palindrome_recurrence(s, c):
    if len(s) == c:
        return ''

    l = r = c

    while 0 <= l and r < len(s) and s[r] == s[l]:
        l -= 1
        r += 1

    l += 1
    r -= 1

    result = s[l:r+1]

    l = r = c
    r += 1

    while 0 <= l and r < len(s) and s[r] == s[l]:
        l -= 1
        r += 1

    l += 1
    r -= 1

    if len(s[l:r+1]) > len(result):
        result = s[l:r+1]

    right_result = longest_palindrome_recurrence(s, c+1)

    if len(result) < len(right_result):
        return right_result

    return result

# Explanation: It memorizes palindrome substrings and when it finds two matching end chars (front & end), it just checks 
#              whether things in the middle is a palindromic substring.
# Run time: O(n^2).  The outer index increases over 's' and the inner index increases from 0 to current outer index
def longest_palindrome_dp(s):
    curr_max = ''
    table = []

    for i in range(len(s)):
        temp = [False] * len(s)
        temp[i] = True
        table.append(temp)

    # ith column, jth row 
    for i in range(len(s)):
        for j in range(len(s)):
            if i == j:
                break
            
            if s[i] == s[j]:
                if (j + 1 < len(s) and table[j+1][i-1] == True) or\
                    i - j == 1:
                    table[j][i] = True

                    if i - j + 1 > len(curr_max):
                        curr_max = s[j:i+1]

    return curr_max
            
input_str = "abcabac"
result = ''

# When length of input_str is shorter than 3, the palindrome substring length can only be one character
if len(input_str) == 1:
    result = input_str[0]
elif len(input_str) > 2:
    #result = longest_palindrome_recurrence(input_str, 0)
    result = longest_palindrome_dp(input_str)

print("intpu: {}, output: {}".format(input_str, result))
