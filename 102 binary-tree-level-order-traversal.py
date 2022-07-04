"""
@Time    : 2022/7/4 17:01
@Author  : 刘俊 jun.liu@deepfinance.com
@File    : 102 binary-tree-level-order-traversal.py

二叉树的层序遍历
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = []
        if root is None:
            return []
        arr = [root]
        while len(arr) > 0:
            ret.append([])
            for i in range(len(arr)):
                node = arr[0]
                ret[len(ret) - 1].append(node.val)
                if node.left is not None:
                    arr.append(node.left)
                if node.right is not None:
                    arr.append(node.right)
                del arr[0]
        return ret
