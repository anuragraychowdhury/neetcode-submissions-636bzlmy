class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_ptr = 0
        t_ptr = 0

        while s_ptr < len(s) and t_ptr < len(t):
            if s[s_ptr] == t[t_ptr]:
                t_ptr += 1
            s_ptr += 1
        
        return len(t) - t_ptr  