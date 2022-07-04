"""
@Time    : 2022/7/4 17:01
@Author  : 刘俊 jun.liu@deepfinance.com
@File    : 102 binary-tree-level-order-traversal.py
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        def level_traversal(root: TreeNode) -> List[List[int]]:
            arr = []

