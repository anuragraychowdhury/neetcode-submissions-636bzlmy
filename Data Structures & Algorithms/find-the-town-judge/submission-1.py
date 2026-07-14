class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = defaultdict(lambda: [0,0]) # person b: (# that trust them, # he trusts)
        for a, b in trust:
            trusted[b][0] += 1
            trusted[a][1] += 1
        
        for i in range(1, n+1):
            if trusted[i][0] == n - 1 and trusted[i][1] == 0:
                return i
        return -1
                