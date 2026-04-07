class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        rank = {}
        for index, letter in enumerate(order):
            rank[letter] = index
        
        for i in range(len(words) - 1):
            word_one = words[i]
            word_two = words[i + 1]

            j = 0
            while j < len(word_one) and j < len(word_two):
                if rank[word_one[j]] < rank[word_two[j]]:
                    break
                elif rank[word_one[j]] > rank[word_two[j]]:
                    return False
                else:
                    j += 1
            
            if j < len(word_one) and j >= len(word_two):
                return False
        return True