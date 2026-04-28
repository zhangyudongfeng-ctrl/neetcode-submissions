class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_pile = max(piles)
        l, r = 1, max_pile
        res = float('inf')
        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i]/mid)
            # mid可行, 继续找有没有更小的数
            if hours <= h:
                r = mid - 1
                res = min(res, mid)
            else: l = mid + 1
        return res


    # def minEatingSpeed(self, piles: List[int], h: int) -> int:
    #     # 暴力法: 在piles中对[1,max(piles[i])]区间内的所有数进行计算作为target
    #     # 二分后续进行优化, 替换外层循环中遍历[1, max(piles[i])]区间的每个数
    #     max_pile = max(piles)
    #     res = float('inf')
    #     for i in range(1, max_pile + 1):
    #         tmp = 0  
    #         for j in range(len(piles)):
    #             target = math.ceil(piles[j] / i)    # target是piles[j]对需要测试的数上取整的结果
    #             tmp += target   # 统计每个待测试数的结果->小时数
    #         # 只在tmp <= h时才算这个数通过测试
    #         if tmp <= h:
    #             # 如果出现一个更小的通过测试数的结果, 更新最终值
    #             res = min(i, res)
    #     return res