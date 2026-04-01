import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if len(s) % 2 == 0:
            l = ((len(s) - 1)) // 2
            r = l + 1
        else:
            l = r = len(s) // 2
        
        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                return False
            l -= 1
            r += 1

        return True
        