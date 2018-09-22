class Solution:
    # Backtracking Solution
    # - Instructions for the characters
    #   1. *: start from 0 instance of previous character
    #   2. .: Go with the ith character that it's looking at in the model string
    #   3. [a-z]: Just match up with the ith character that it's looking at in the model string
    def backtracking_sol(self, s, p, curr, i):
        print(s,p,curr,i)
        if s == curr and i == len(p):
            return True

        if len(s) < len(curr) or len(p) <= i:
            return False

        option1 = option2 = option3 = option4 = option5 = option6 = option7 = False

        if p[i] == '.':
            option3 = self.backtracking_sol(s, p, curr + s[len(curr)], i+1)
        elif p[i] == '*':
            if i == 0:
                option4 = self.backtracking_sol(s, p, curr, i+1)
            elif i > 0:
                if s[len(curr)] == p[i-1] or p[i-1] == '.':
                    option5 = self.backtracking_sol(s, p, curr + s[len(curr)], i)
                    option6 = self.backtracking_sol(s, p, curr + s[len(curr)], i+1)
                else: # aab - c*a*b : when i == 1, it doesn't want to populate c in front of it so it should
                      # just pass that and go on to the a
                    option7 = self.backtracking_sol(s, p, curr, i+1)
        else:
            if p[i] == s[len(curr)]:
                option1 = self.backtracking_sol(s, p, curr + p[i], i+1)
            elif i + 1 < len(p) and p[i + 1] == '*': # Trying out to see if this could work
                option2 = self.backtracking_sol(s, p, curr, i+1)
            else:
                return False

        if option1 or option2 or option3 or option4 or option5 or option6 or option7:
            return True
        
        return False
            
    def isMatch(self, s, p):
        return self.backtracking_sol(s, p, "", 0)

sol = Solution()
#print(sol.isMatch('aa', 'a'))
#print(sol.isMatch('aa', 'a*'))
#print(sol.isMatch('ab', '.*'))
#print(sol.isMatch('aab', 'c*a*b'))
#print(sol.isMatch('mississippi', 'mis*is*p*'))
print(sol.isMatch('ab','.*c'))
