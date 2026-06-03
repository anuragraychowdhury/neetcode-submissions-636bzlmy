class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate_one = None
        candidate_two = None
        count_one = 0
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
                if count_one == 0:
                    candidate_one = None
                if count_two == 0:
                    candidate_two = None
        
        res = []
        if nums.count(candidate_one) > len(nums)//3:
            res.append(candidate_one)
        if nums.count(candidate_two) > len(nums)//3:
            res.append(candidate_two)
        return res
            
            