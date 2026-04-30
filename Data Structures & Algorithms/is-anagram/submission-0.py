class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 思路: 统计s中字符的出现次数, 遍历t, 遇到出现的字符就减去1次, 最后看map_s是否为空
        map_s = {}
        for c in s:
            map_s[c] = map_s.get(c, 0) + 1
        for c in t:
            map_s[c] = map_s.get(c, 0) - 1
        # 如果相同次数, map_s{s:0, t:0}这种
        return all(v == 0 for v in map_s.values())
        
