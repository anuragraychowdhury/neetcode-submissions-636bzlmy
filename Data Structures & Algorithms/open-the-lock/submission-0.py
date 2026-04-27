class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1 
        
        visited = set(deadends)
        q = deque()
        q.append(['0000', 0])
        visited.add('0000')

        while q:
            code, moves = q.popleft()
            
            if code == target:
                return moves
            
            for i in range(4):
                positive_digit = (int(code[i]) + 1) % 10
                negative_digit = (int(code[i]) - 1) % 10
                
                positive_code = code[:i] + str(positive_digit) + code[i+1:]
                negative_code = code[:i] + str(negative_digit) + code[i+1:]

                if positive_code not in visited:
                    visited.add(positive_code)
                    q.append([positive_code, moves + 1])
                if negative_code not in visited:
                    visited.add(negative_code)
                    q.append([negative_code, moves + 1])
        
        return -1