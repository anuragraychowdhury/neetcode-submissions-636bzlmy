class Solution:

    def __init__(self, w: list[int]):
        self.prefix = []
        running_sum = 0
        self.sum = sum(w)
        for number in w:
            running_sum += number
            self.prefix.append(running_sum)

    def pickIndex(self) -> int:
        picked_index = random.randint(0, self.sum - 1)
        left = 0 
        right = len(self.prefix) - 1

        while left < right:
            middle = (left + right) // 2
            if picked_index < self.prefix[middle]:
                right = middle
            else:
                left = middle + 1
        return left

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()