# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # 用栈模拟
        if not root:
            return []
        q = deque()
        q.append(root)
        res = []
        level = 0
        # 外层遍历层数
        while q:
            level += 1
            level_res = []

            # 内层遍历节点
            for i in range(len(q)):
                node = q.popleft()
                level_res.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(level_res)
        return res 
