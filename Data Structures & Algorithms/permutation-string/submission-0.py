class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = {}
        for letter in s1:
            freq[letter] = freq.get(letter,0) + 1
        
        for i in range(len(s2) - len(s1) + 1):
            window = s2[i: i + len(s1)]
            windowFreq = {}
            for letter in window:
                windowFreq[letter] = windowFreq.get(letter, 0) + 1
            if windowFreq.items() == freq.items():
                return True
        
        return False
