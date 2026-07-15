class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res = []

        def word_finder(index, subset):
            if index == len(s):
                res.append(" ".join(subset))
                return
            
            for i in range(1, len(s) - index + 1):
                prefix = s[index:index + i]
                if prefix in wordDict:
                    subset.append(prefix)
                    word_finder(index + i, subset)
                    subset.pop()
            return
        
        word_finder(0,[])
        return res


        
        

                    