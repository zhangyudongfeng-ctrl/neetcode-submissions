class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 和上一题的区别是什么? -> 上一题是找第一个不满足递增的数, 这题需要在找到这个数的基础上, 以这个数作为2段区间划分的标准
        # 之后target和nums[0]进行判断, if target > nums[0], 说明在左区间寻找, else 说明在右区间里, 再次进行二分

        # 第一次二分,找到第一个不满足递增的数
        range_l, range_r = 0, len(nums) - 1
        while range_l < range_r:
            pos = (range_l + range_r) // 2  
            if nums[pos] > nums[range_r]: range_l = pos + 1
            else: range_r = pos 
        flag = range_l  # 找到区间分割点索引下标
        if flag == 0:   # 数组没有旋转
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target: l = mid + 1
                elif nums[mid] > target: r = mid - 1
                else: return mid
        elif target >= nums[0]:
            # 说明在左区间[0, flag - 1]
            l, r = 0, flag - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target: l = mid + 1
                elif nums[mid] > target: r = mid - 1
                else: return mid
        else:
            # 说明在右区间里[flag, len(nums) - 1]
            l, r = flag, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target: l = mid + 1
                elif nums[mid] > target: r = mid - 1
                else: return mid
        return -1 
