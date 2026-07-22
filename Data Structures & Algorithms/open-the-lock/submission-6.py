class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        
        queue = deque()
        queue.append('0000')
        visited = set()
        turns = 0

        while queue:
            size = len(queue)
            for i in range(size):
                comb = queue.popleft()
                if comb == target:
                    return turns
                
                for i in range(len(comb)):
                    digit_up = (int(comb[i]) + 1) % 10
                    up_comb = comb[:i] + str(digit_up) + comb[i+1:]

                    digit_down = (int(comb[i]) - 1) % 10
                    down_comb = comb[:i] + str(digit_down) + comb[i+1:]

                    if up_comb not in deadends and up_comb not in visited:
                        queue.append(up_comb)
                        visited.add(up_comb)
                    if down_comb not in deadends and down_comb not in visited:
                        queue.append(down_comb)
                        visited.add(down_comb)
            turns += 1
        return -1    
                                        