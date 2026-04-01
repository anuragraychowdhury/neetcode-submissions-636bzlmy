class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            arrival_time = (target - position[i]) / speed[i]
            cars.append((position[i], arrival_time))
        
        cars.sort(reverse = True)

        stack = []

        for pos, time in cars:
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)