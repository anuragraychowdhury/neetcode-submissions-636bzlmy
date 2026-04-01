class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        if not s or not t:
            return ""

        t_map = Counter(t)
        min_len = float('inf')
        result = ""

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                window = s[i:j]
                window_map = Counter(window)

                # Check if window contains all characters in t
                valid = True
                for ch in t_map:
                    if window_map[ch] < t_map[ch]:
                        valid = False
                        break

                if valid and (j - i) < min_len:
                    min_len = j - i
                    result = window

        return result