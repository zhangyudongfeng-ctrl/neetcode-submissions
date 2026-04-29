class TimeMap:
    # 思路: alice: 1, 3 -> 假设来一个alice, 2, 需要返回2前一个时间戳的key, 也就是alice,1 ,如果来一个alice, 4, 需要返回它前一个时间戳的key, 也就是alice, 3
    # 期望的数据结构: self.map = {"alice": [(1, "happy"), (3, "sad")]}
    def __init__(self):
        # 需要一个哈希用于插入和查找,因为哈希一个key不能同时保存2个值,会覆盖, 所以在哈希内部需要使用set. 还需要这个val对应的时间戳
        self.map = defaultdict(list)    # key -> [(timestamp, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        # 此时key还不存在, 先创建空列表再添加, 这是map = {}的写法, 需要判断, 如果使用defaultdict不需要判断
        # if key not in self.map:
        #     self.map[key] = []
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.map.get(key, [])
        if not arr: return ""
        # arr内容: [(1, happy), (3, sad)]
        # 需要对内部的prev_timestamp进行二分, 找什么值? -> 找prev_timestamp<=当前timestamp的最后一个值
        l, r = 0, len(arr) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            prev_t, v = arr[mid]
            # 1, 3, 5  -> 4, 可能mid是1, 找到了确实符合条件, 但不是最新的时间, 再去右边看看
            # 说明找到了, 就是这个v
            if prev_t <= timestamp:
                res = v
                l = mid + 1
            # 时间大了 prev_t > timestamp, 去左边寻找
            else:
                r = mid - 1
        return res

