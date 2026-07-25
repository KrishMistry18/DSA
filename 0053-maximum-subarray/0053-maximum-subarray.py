class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna