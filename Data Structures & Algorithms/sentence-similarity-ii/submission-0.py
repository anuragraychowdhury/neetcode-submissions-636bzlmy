class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        words = {word for pair in similarPairs for word in pair}
        word_parents = {}
        for word in words:
            word_parents[word] = word
        
        rank = {}
        for word in word_parents:
            rank[word] = 1

        def find(word):
            while word != word_parents[word]:
                word = find(word_parents[word])
            return word 
            # path = []
            # while word != word_parents[word]:
            #     path.append(word)
            #     word = word_parents[word]
            # for node in path:
            #     word_parents[node] = word
            # return word
        
        def union(word1, word2):
            parent1 = find(word1)
            parent2 = find(word2)

            if parent1 == parent2:
                return True
            
            if rank[parent1] >= rank[parent2]:
                rank[parent1] += rank[parent2]
                word_parents[parent2] = word_parents[parent1]
            else:
                rank[parent2] += rank[parent1]
                word_parents[parent1] = word_parents[parent2]
        
        for pair in similarPairs:
            union(pair[0], pair[1])
        
        if len(sentence1) != len(sentence2):
            return False
        
        for word_one, word_two in zip(sentence1, sentence2):
            if word_one == word_two:
                continue
            if word_one not in word_parents or word_two not in word_parents:
                return False
            if find(word_one) != find(word_two):
                return False
        return True


        