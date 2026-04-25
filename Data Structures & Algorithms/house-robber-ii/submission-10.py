class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def robbing(start_index, end_index):
            new_arr = nums[start_index:end_index]
            if len(new_arr) == 0:
                return 0
            if len(new_arr) == 1:
                return new_arr[0]
            
            dp = [0] * len(new_arr)
            dp[0] = new_arr[0]
            dp[1] = max(dp[0], new_arr[1])
            for i in range(2, len(new_arr)):
                dp[i] = max(new_arr[i] + dp[i-2], dp[i-1])
            return dp[-1]
        
        res1 = robbing(0, len(nums) - 1)
        res2 = robbing(1, len(nums))

        return max(res1, res2)
