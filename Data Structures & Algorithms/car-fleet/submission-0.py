class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            arrival_time = (target - position[i]) / speed[i]
            cars.append((position[i], arrival_time))
        
        cars.sort(reverse = True)

        fleets = 1

        curr_time = cars[0][1]

        for i in range(1, len(cars)):
            pos, time = cars[i]
            if time > curr_time:
                fleets += 1
                curr_time = time
        return fleets