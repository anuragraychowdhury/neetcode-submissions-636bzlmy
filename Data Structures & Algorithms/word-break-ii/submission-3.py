class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res = []
        def find_words(index, subset):
            if index == len(s):
                res.append(" ".join(subset))
                return
                
            for i in range(1, len(s) - index + 1):
                prefix = s[index:index + i]
                if prefix in wordDict:
                    subset.append(prefix)
                    find_words(index + i, subset)
                    subset.pop()
            return 
        
        find_words(0, [])
        return res
        
        

                    