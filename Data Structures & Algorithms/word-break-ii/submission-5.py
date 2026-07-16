class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res = []

        def word_finder(index, subset):
            if index == len(s):
                res.append(" ".join(subset))
                return
            
            for i in range(index, len(s)):
                prefix = s[index: i+1]
                if prefix in wordDict:
                    subset.append(prefix)
                    word_finder(i+1, subset)
                    subset.pop()
            return
        
        word_finder(0,[])
        return res


        
        

                    