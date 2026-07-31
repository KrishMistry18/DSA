class Solution(object):
    def maxAbsoluteSum(self, nums):
        best_max = nums[0]
        best_min = nums[0]
        ans = abs(nums[0])

        for i in range(1, len(nums)):
            best_max = max(nums[i], best_max + nums[i])
            best_min = min(nums[i], best_min + nums[i])

            ans = max(ans, max(abs(best_max),abs(best_min)))

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna