class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
        
        q = deque()
        q.append('0000')
        turns = 0
        visited = set()

        while q:
            size = len(q)
            for i in range(size):
                candidate_code = q.popleft()
                if candidate_code == target:
                    return turns
                
                for i in range(len(candidate_code)):
                    down_char = (int(candidate_code[i]) + 1) % 10
                    down_code = candidate_code[:i] + str(down_char) + candidate_code[i+1:]

                    up_char = (int(candidate_code[i]) - 1) % 10
                    up_code = candidate_code[:i] + str(up_char) + candidate_code[i+1:]

                    if up_code not in visited and up_code not in deadends:
                        q.append(up_code)
                        visited.add(up_code)
                    if down_code not in visited and down_code not in deadends:
                        q.append(down_code)
                        visited.add(down_code)
            turns += 1
        return -1
                    