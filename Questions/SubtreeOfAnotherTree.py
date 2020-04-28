'''
Subtree of Another Tree
'''
'''
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with
a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.
'''
# Example 1:
s = [3,4,5,1,2]
t = [4,1,2]
# Given tree s:
#      3
#     / \
#    4   5
#   / \
#  1   2
# Given tree t:
#    4
#   / \
#  1   2
# Return true, because t has the same structure and node values with a subtree of s.

# Example 2:
# Given tree s:
#
#      3
#     / \
#    4   5
#   / \
#  1   2
#     /
#    0
# Given tree t:
#    4
#   / \
#  1   2
# Return false.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution(object):
	def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
		def sub(s, t, started=False):
			if not s:
				return not t

			if not t:
				return not s

			if s.val != t.val:
				if started:
					return False
				return sub(s.left, t, started) or sub(s.right, t, started)

			if s.val == t.val:
				return (sub(s.left, t.left, 1) and sub(s.right, t.right, 1)) or (
							sub(s.left, t, 0) or sub(s.right, t, 0))

			return False

		return sub(s, t)
