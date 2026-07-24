class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        if s_len != t_len:
            return False
        map = {}
        for i in range(s_len):
            map[s[i]] = 1 + map.get(s[i], 0)
            map[t[i]] = map.get(t[i], 0) - 1
        
        for i in range(s_len):
            if map[s[i]] != 0:
                return False

        return True
        