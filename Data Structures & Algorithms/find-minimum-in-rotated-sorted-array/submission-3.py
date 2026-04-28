class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 用二分去找不满足递增顺序的数, 递增顺序: nums[i] > nums[i-1]
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            # 存在2个递增区间
            # 说明在右边区间, 而且l这个值不可能是最小值, 所以可以+1
            if nums[mid] > nums[r]: l = mid + 1 
            # else情况 nums[mid] <= nums[r]
            # 最小值在 mid 前面
            # nums = [5, 0, 1, 2, 3, 4]
            #                 ^
            #                mid
            else: r = mid 
        return nums[l]