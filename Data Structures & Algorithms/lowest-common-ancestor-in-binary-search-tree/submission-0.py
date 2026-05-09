# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        如何判断2个节点的最近公共祖先?
        1.p是祖先, q是p的子节点, return p
        2.q是祖先, p是q的子节点, return q
        3.p/q都是某个祖先node的子节点, return node
                    ↓
        需要设计一个递归函数, 入参是3个节点root, p和q, 判断p/q是否同边 -> 可以更简单, 直接用原函数 -> 返回 p 和 q 的 LCA
            - if root.val > p.val and root.val > q.val 
                - 同边, 且pq都在左子树, 递归左子树
            - if root.val < p.val and root.val < q.val 
                - 同边, 且pq都在右子树, 递归右子树
            - else
                - p/q不同边, return root
        """
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        