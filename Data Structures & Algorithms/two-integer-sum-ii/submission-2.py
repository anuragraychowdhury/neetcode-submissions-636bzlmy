class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # binary search
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]

            while l <= r:
                midpoint = (l + r) // 2
                if numbers[midpoint] < tmp:
                    l = midpoint + 1
                elif numbers[midpoint] > tmp:
                    r = midpoint - 1
                else:
                    return [i + 1, midpoint + 1]
        return []
        # two-ptr

        # l = 0
        # r = len(numbers) - 1

        # while l < r:
        #     curr = numbers[l] + numbers[r]
            
        #     if curr == target:
        #         return [l+1,r+1]
        #     elif curr < target:
        #         l += 1
        #     else:
        #         r -= 1
        # return []
