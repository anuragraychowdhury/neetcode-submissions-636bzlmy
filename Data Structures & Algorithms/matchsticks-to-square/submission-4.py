class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort()
        if sum(matchsticks) % 4 != 0:
            return False
        one_side = sum(matchsticks) // 4
        used = [False] * len(matchsticks)
        
        def find_side(curr_val, total):
            if total == 0:
                return True
            if curr_val > one_side:
                return False
            if curr_val == one_side:
                total -= 1
                curr_val = 0
                return find_side(curr_val, total)
            
            for i in range(len(matchsticks)):
                if i > 0 and used[i-1] == False and matchsticks[i-1] == matchsticks[i]:
                    continue
                if used[i] == True:
                    continue
                curr_val += matchsticks[i]
                used[i] = True
                
                side_check = find_side(curr_val, total)
                if side_check == True:
                    return True
                else:
                    curr_val -= matchsticks[i]
                    used[i] = False
            return False
        
        res = find_side(0, 4)
        return res

        



