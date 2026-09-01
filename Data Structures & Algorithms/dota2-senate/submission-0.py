class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        n = len(senate)

        for i,c in enumerate(senate):
            if c == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            if radiant[0] < dire[0]:
                dire.popleft()
                index = radiant.popleft()
                radiant.append(index + n)
            else:
                radiant.popleft()
                index = dire.popleft()
                dire.append(index + n)
        
        if radiant:
            return "Radiant"
        else:
            return "Dire"