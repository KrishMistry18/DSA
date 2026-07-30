class Solution(object):
    def maxProduct(self, nums):
        i = 0
        best_max = nums[i]
        best_min = nums[i]
        ans = nums[i]

        for i in range(1,len(nums)):
            v1 = nums[i]
            v2 = best_max * nums[i]
            v3 = best_min * nums[i]

            best_max = max(v1,max(v2,v3))
            best_min = min(v1,min(v2,v3))

            ans = max(ans,max(best_max,best_min))

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna