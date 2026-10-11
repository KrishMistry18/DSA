class Solution(object):
    def sumOfSquares(self, nums):
        n = len(nums)
        total = 0

        for i in range(1, n + 1):
            if n % i == 0:
                total += nums[i - 1] * nums[i - 1]

        return total

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna