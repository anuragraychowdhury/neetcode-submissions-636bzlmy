class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        if sum(matchsticks) % 4 != 0:
            return False
        one_side = sum(matchsticks) // 4
        
        buckets = [0] * 4
        def find_side(index, buckets):
            if index == len(matchsticks):
                for i in range(len(buckets)):
                    if buckets[i] != one_side:
                        return False
                return True
            
            for j in range(len(buckets)):
                if buckets[j] + matchsticks[index] > one_side:
                    continue
                else:
                    buckets[j] += matchsticks[index]
                    side_check = find_side(index + 1, buckets)
                    if side_check == True:
                        return True
                    else:
                        buckets[j] -= matchsticks[index]
            return False
        res = find_side(0, buckets)
        return res

        



