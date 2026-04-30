# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 反转左右子节点, 再反转左右子节点的子节点 -> 递归调用该函数, 返回的是翻转后的父节点
        # 终止条件, 遇上空节点, 说明不用继续反转了
        if not root: return None 
        tmp = root.right 
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(tmp)
        return root 