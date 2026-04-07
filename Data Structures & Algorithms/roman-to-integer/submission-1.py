class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        i = 0
        total = 0
        while i < len(s) - 1:
            if mapping[s[i]] < mapping[s[i + 1]]:
                total += (mapping[s[i + 1]] - mapping[s[i]])
                i += 2
            else:
                total += mapping[s[i]]
                i += 1
        
        if i <= len(s) - 1:
            total += mapping[s[i]]

        return total