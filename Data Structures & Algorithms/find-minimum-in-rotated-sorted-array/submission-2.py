class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 旋转N次 -> 把数组的最后N个元素移到数组开头, 但是不知道旋转了几次
        # 需要把数组分为2部分
        if len(nums) == 1: return nums[0]
        for i in range(1, len(nums)):
            # 如果没保持递增, 说明找到结果了
            if nums[i] < nums[i-1]: return nums[i]
            # 如果保持递增到最后一个为止, 返回第一个数
            else:
                if i == len(nums) - 1: return nums[0]
