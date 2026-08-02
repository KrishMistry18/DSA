from fractions import gcd

class Solution(object):
    def maxPairStrength(self, nums):
        ans = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                g = gcd(nums[i], nums[j])
                strength = (nums[i] * nums[j]) // (g * g)
                ans = max(ans, strength)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna