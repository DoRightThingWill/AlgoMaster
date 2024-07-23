class Solution:
    def jump(self, nums: List[int]) -> int:
        # f(n) = min (
            # direct jump from n - 1
                # if nums[n-1] >= 1, f(n-1) + 1
            # direct jump from n - 2
                # if nums[n-2] >= 2, f(n-2) + 1
            # direct jump from n - 3
            # ... 
        # )

        # nums = [2,3,1,1,4]
        #         0,1,2,3,4
        # dp =   [0,1,1,2,]
        # min_jump = 1
        # i = 3
        # #   j = 0
        #     nums[0] = 2 , i - j = 3 
        # #   j = 1
        #     nums[1] = 3, i - j = 2
        #     min = dp[1] + 1= 2
        # #   j = 2
        #     nums[2] =  1, i - j = 1
        #     dp[2] + 1 = 1 + 1= 2
        #     min = 2

        dp = [0]

        for i in range(1, len(nums)):
            min_jump = float("inf")
            for j in range(0, i):
                if nums[j] >= i - j: 
                    min_jump = min(min_jump, dp[j] + 1)
            
            dp.append(min_jump)
        
        return dp[-1]



            
