class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        if sum(nums) % k != 0:
            return False
        side_length = sum(nums) // k
        buckets = [0] * k

        def recurse_side_value(index):
            if index == len(nums):
                for j in range(len(buckets)):
                    if buckets[j] != side_length:
                        return False
                return True

            for i in range(len(buckets)):
                if buckets[i] + nums[index] > side_length:
                    continue
                else:
                    buckets[i] += nums[index] 
                    if recurse_side_value(index + 1) == True:
                        return True
                    else:
                        buckets[i] -= nums[index]
                        if buckets[i] == 0:
                            break
            return False
        
        return recurse_side_value(0)
        
        
                        


