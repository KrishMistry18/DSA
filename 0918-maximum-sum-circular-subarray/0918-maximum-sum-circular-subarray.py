class Solution(object):
    def maxSubarraySumCircular(self, nums):
        best = nums[0]
        worst = nums[0]
        sum = nums[0]
        ans = nums[0]

        normal_max = nums[0]
        normal_min = nums[0]

        for i in range(1,len(nums)):
            sum += nums[i]

            best = max(best + nums[i], nums[i])
            normal_max = max(normal_max, best)

            worst = min (worst + nums[i], nums[i])
            normal_min = min(normal_min, worst)            

        if normal_max < 0:
            return normal_max
        
        return max(normal_max,sum - normal_min)



        
        
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna