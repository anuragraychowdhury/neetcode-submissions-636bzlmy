class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map = {}
        map2 = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            print(s[i])
            map[s[i]] = map.get(s[i],0) + 1
            map2[t[i]] = map2.get(t[i],0) + 1

        return sorted(map.items()) == sorted(map2.items())



