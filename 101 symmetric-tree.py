"""
@Time    : 2022/7/4 16:33
@Author  : 刘俊 jun.liu@deepfinance.com
@File    : 101 symmetric-tree.py

对称二叉树
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:


        def checkSymmetric(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            if not root1 and not root2:
                return True
            elif not root1 or not root2:
                return False
            elif root1.val != root2.val:
                return False
            else:
                return checkSymmetric(root1.left, root2.right) and checkSymmetric(root1.right, root2.left)

        return checkSymmetric(root.left, root.right)
