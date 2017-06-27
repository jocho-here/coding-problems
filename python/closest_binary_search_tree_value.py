import sys

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        curr = root
        diff = sys.maxint
        closest_one = curr
        
        while curr != None:
            new_diff = abs(curr.val - target)
            
            if new_diff < diff:
                closest_one = curr
                diff = new_diff
            
            if target < curr.val:
                curr = curr.left
            elif target > curr.val:
                curr = curr.right
            else:
                break
            
        return closest_one.val