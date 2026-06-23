class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        buckets = [0] * k
        total = sum(nums)
        if total % k != 0:
            return False
        subset = total // k

        def subset_placement(index):
            if index == len(nums):
                for bucket in buckets:
                    if bucket != subset:
                        return False
                return True
            
            for i in range(len(buckets)):
                if buckets[i] + nums[index] > subset:
                    continue
                else:
                    buckets[i] += nums[index]
                    next_call = subset_placement(index + 1)
                    if next_call == True:
                        return True
                    else:
                        buckets[i] -= nums[index]
                        if buckets[i] == 0:
                            break
            return False
        
        return subset_placement(0)


