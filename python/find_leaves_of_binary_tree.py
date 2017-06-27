# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def findLeaves(self, root):
		result_dict = {}

		if root != None:
			top_level = find_node_levels(result_dict, root)

		return result_dict.values()
    
	def find_node_levels(self, result_dict, curr_node):
		curr_level = 0

		if curr_node.left != None:
			curr_level = find_node_levels(result_dict, curr_node.left) + 1

		if curr_node.right != None:
			level_right = find_node_levels(result_dict, curr_node.right) + 1

			if level_right > curr_level:
				curr_level = level_right

		if result_dict.has_key(curr_level):
			result_dict[curr_level].append(curr_node.val)
		
		else:
			result_dict[curr_level] = [curr_node.val]

		return curr_level
