class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        num_to_trusted = {}
        for i in range(n + 1):
            num_to_trusted[i] = set()
        
        for a,b in trust:
            num_to_trusted[a].add(b)
        
        for number, trusts in num_to_trusted.items():
            if len(trusts) == 0:
                potential = number
        
        tally = 0
        for number, trusts in num_to_trusted.items():
            if number == potential:
                continue
            elif potential in num_to_trusted[number]:
                tally += 1
        
        if tally == n - 1:
            return potential
        else:
            return -1
        
            
        


