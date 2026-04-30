class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = defaultdict(int)
        # 记录每个元素对应的下标
        for i in range(len(nums)):
            map[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in map and map[target - nums[i]] != i:
                return [i, map[target - nums[i]]]
        return []                