class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}
        for letter in t:
            t_dict[letter] = t_dict.get(letter, 0) + 1
        
        have = 0
        need = len(t_dict)

        left = 0
        right = 0
        
        min_window = float('inf')
        min_substr = ""

        while right < len(s):
            curr_char = s[right]
            if curr_char in t_dict:
                t_dict[curr_char] -= 1
                if t_dict[curr_char] == 0:
                    have += 1
                
                while have == need:
                    if right - left + 1 < min_window:
                        min_window = right - left + 1
                        min_substr = s[left:right + 1]
                    
                    left_char = s[left]
                    if left_char in t_dict:
                        t_dict[left_char] += 1
                    left += 1

                    if left_char in t_dict and t_dict[left_char] > 0:
                        have -= 1
            right += 1
        return min_substr