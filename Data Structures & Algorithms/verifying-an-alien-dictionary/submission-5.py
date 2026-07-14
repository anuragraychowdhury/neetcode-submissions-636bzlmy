class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_dict = {}
        for index, letter in enumerate(order):
            alien_dict[letter] = index
        
        for i in range(len(words) - 1):
            word_one = words[i]
            word_two = words[i+1]
            
            j = 0
            while j < len(word_one) and j < len(word_two):
                if word_one[j] != word_two[j]:
                    if alien_dict[word_one[j]] > alien_dict[word_two[j]]:
                        return False
                    break
                j += 1
            else:
                if len(word_one) > len(word_two):
                    return False
        return True

            

