class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if '0000' in deadends or target in deadends:
            return -1
        queue = deque(['0000'])
        visited = {'0000'}
        turns = 0

        while queue:
            size = len(queue)
            for i in range(size):
                code = queue.popleft()
                
                if code == target:
                    return turns
                
                for i in range(len(code)):
                    digit_pos = (int(code[i]) + 1) % 10
                    new_pos_code = code[:i] + str(digit_pos) + code[i+1:]

                    digit_neg = (int(code[i]) - 1) % 10
                    new_neg_code = code[:i] + str(digit_neg) + code[i+1:]

                    if new_pos_code not in visited and new_pos_code not in deadends:
                        visited.add(new_pos_code)
                        queue.append(new_pos_code)
                    if new_neg_code not in visited and new_neg_code not in deadends:
                        visited.add(new_neg_code)
                        queue.append(new_neg_code)

            turns += 1
        return -1

                    
