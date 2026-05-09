class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate_one = None
        count_one = 0
        candidate_two = None
        count_two = 0

        for number in nums:
            if number == candidate_one:
                count_one += 1
            elif number == candidate_two:
                count_two += 1
            
            elif count_one == 0:
                candidate_one = number
                count_one += 1
            elif count_two == 0:
                candidate_two = number
                count_two += 1
            
            else:
                count_one -= 1
                count_two -= 1
        
        res = []
        
        for c in [candidate_one, candidate_two]:
            if nums.count(c) > len(nums) // 3:
                res.append(c)
        return res