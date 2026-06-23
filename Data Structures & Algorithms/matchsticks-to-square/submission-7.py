class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        buckets = [0] * 4
        total = sum(matchsticks)
        
        if total % 4 != 0:
            return False
        
        square_side = total // 4
        matchsticks.sort(reverse=True)

        def place_matchstick(match_index):
            # if we reach the end of the matchsticks, we have an assortment of matchsticks to check
            if match_index == len(matchsticks):
                for bucket in buckets:
                    if bucket != square_side:
                        return False
                return True

            for i in range(len(buckets)):
                if buckets[i] + matchsticks[match_index] > square_side:
                    continue
                else:
                    buckets[i] += matchsticks[match_index]
                    next_call = place_matchstick(match_index + 1)
                    if next_call == True:
                        return True
                    else:
                        buckets[i] -= matchsticks[match_index]
                        if buckets[i] == 0:
                            break
            return False
        
        res = place_matchstick(0)
        return res
