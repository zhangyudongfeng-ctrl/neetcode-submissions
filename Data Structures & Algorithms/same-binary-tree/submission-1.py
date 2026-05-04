# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # 判断p和q两棵树是否相等
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # p非空, q空
        if p and not q: return False
        # p空, q非空
        elif not p and q: return False
        # p, q都空
        elif not p and not q: return True 
        # p, q都不空 -> 递归判断左右子树
        else:
            if p.val != q.val:
                return False 
            else:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

