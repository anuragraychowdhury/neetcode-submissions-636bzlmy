class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            lst_key = [0] * 26
            for i in range(len(s)):
                lst_key[ord(f'{s[i]}') - ord('a')] += 1
            tuple_key = tuple(lst_key)
            anagrams[tuple_key].append(s)
        
        res = []
        for key, value in anagrams.items():
            res.append(value)
        return res
            