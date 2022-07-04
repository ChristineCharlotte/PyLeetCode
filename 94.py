"""
@Time    : 2022/7/4 15:59
@Author  : 刘俊 jun.liu@deepfinance.com
@File    : 94.py

二叉树的中序遍历
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def inorder(root):
            if root is None:
                return
            root.left = inorder(root.left)
            res.append(root.val)
            root.right = inorder(root.right)
            return

        inorder(root)
        return res