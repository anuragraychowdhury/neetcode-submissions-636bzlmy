class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordering = {}
        for i in range(len(order)):
            ordering[order[i]] = i
        
        for i in range(len(words) - 1):
            word_one = words[i]
            word_two = words[i + 1]

            word_one_ptr = 0
            word_two_ptr = 0

            while word_one_ptr < len(word_one) and word_two_ptr < len(word_two):
                if ordering[word_one[word_one_ptr]] < ordering[word_two[word_two_ptr]]:
                    break
                elif ordering[word_one[word_one_ptr]] > ordering[word_two[word_two_ptr]]:
                    return False
                else:
                    word_one_ptr += 1
                    word_two_ptr += 1
            
            if word_one_ptr < len(word_one) and word_two_ptr >= len(word_two):
                return False
        return True

            
            


