class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 这题就相当于是多维二分查找
        # 2次二分, 第一次二分粗略划定范围, 找在哪个行中寻找target, 第二次二分进行详细寻找target
        m, n = len(matrix), len(matrix[0])
        top, bot = 0, m - 1
        target_row = -1
        while top <= bot:
            row = (top + bot) // 2
            # 如果target > 这行最后一个数, 说明需要在下一行中寻找, 更新top
            if target > matrix[row][-1]: top = row + 1
            # 如果target < 这行第一个数, 说明需要在上一行中寻找, 更新bot
            elif target < matrix[row][0]: bot = row - 1
            # 否则, 找到结果, 直接break, 进行第二次二分
            else: 
                target_row = row 
                break

        if top > bot:
            return False
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[target_row][m]: l = m + 1
            elif target < matrix[target_row][m]: r = m - 1
            else: return True 
        return False  
        