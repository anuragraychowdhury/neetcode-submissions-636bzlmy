class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for number in nums:
            if count == 0:
                candidate = number
                count += 1
                continue
            elif number == candidate:
                count += 1
            else:
                count -= 1
        return candidate