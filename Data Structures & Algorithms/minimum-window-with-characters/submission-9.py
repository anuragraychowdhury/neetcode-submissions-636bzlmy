class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        t_dict = {}
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1
        
        left = 0
        t_dict_count = len(t_dict.keys())
        min_cnt = float('inf')
        minimum_substr = ""

        for right in range(len(s)):
            if s[right] in t_dict:
                t_dict[s[right]] -= 1
                if t_dict[s[right]] == 0:
                    t_dict_count -= 1
            
            while t_dict_count == 0:
                if s[left] in t_dict:
                    t_dict[s[left]] += 1
                    if t_dict[s[left]] > 0:
                        t_dict_count += 1
                
                if right - left + 1 < min_cnt:
                    minimum_substr = s[left:right + 1]
                    min_cnt = right - left + 1
                
                left += 1
        
        return minimum_substr




        
