class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_dict = {}
        t_dict = {}

        for letter in s:
            s_dict[letter] = s_dict.get(letter,0) + 1
        for letter in t:
            t_dict[letter] = t_dict.get(letter,0) + 1
        
        for key in s_dict:
            if key not in t_dict or s_dict[key] != t_dict[key]:
                return False
        
        for key in t_dict:
            if key not in s_dict:
                return False

        return True