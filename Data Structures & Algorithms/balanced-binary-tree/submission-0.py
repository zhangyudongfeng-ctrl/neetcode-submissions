# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        # 递归函数定义: - 如果 node 这棵子树平衡：返回它的高度; 如果 node 这棵子树不平衡：返回 -1
        def dfs(node: Optional[TreeNode]) -> int:
            # 空节点高度就是0
            if not node: return 0

            left_height = dfs(node.left)
            if left_height == -1:
                return -1
            right_height = dfs(node.right)
            if right_height == -1:
                return -1
            if abs(left_height - right_height) > 1: return -1
            return max(left_height, right_height) + 1
        
        return dfs(root) != -1 
