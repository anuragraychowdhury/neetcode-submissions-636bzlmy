class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    return [left, right]
                else:
                    left -= 1
                    right += 1
            return [left, right]
        
        max_len = 0
        curr_max_left = None
        curr_max_right = None

        for i in range(len(s)):
            odd_pote_left, odd_pote_right = expand(i, i)
            even_pote_left, even_pote_right = expand(i, i + 1)

            if even_pote_right - even_pote_left + 1 > max_len:
                curr_max_left = even_pote_left
                curr_max_right = even_pote_right
                max_len = even_pote_right - even_pote_left + 1
            
            if odd_pote_right - odd_pote_left + 1 > max_len:
                curr_max_left = odd_pote_left
                curr_max_right = odd_pote_right
                max_len = odd_pote_right - odd_pote_left + 1
        
        return s[curr_max_left + 1: curr_max_right]