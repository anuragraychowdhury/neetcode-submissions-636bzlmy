class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        t_dict = {}
        for elem in t:
            t_dict[elem] = t_dict.get(elem, 0) + 1
        
        count = 0
        for key in t_dict.keys():
            count += 1
        
        left = 0
        best = ["", float('inf')]
        for right in range(len(s)):
            if s[right] in t_dict:
                t_dict[s[right]] -= 1
                if t_dict[s[right]] == 0:
                    count -= 1
                
                while count == 0:
                    if right - left + 1 < best[1]:
                        best[1] = right - left + 1
                        best[0] = s[left:right+1]
                    if s[left] in t_dict:
                        t_dict[s[left]] += 1
                        if t_dict[s[left]] > 0:
                            count += 1
                        left += 1
                    else:
                        left += 1
        return best[0]



