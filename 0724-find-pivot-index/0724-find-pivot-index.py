class Solution(object):
    def pivotIndex(self, nums):
        left = 0
        total = 0

        for i in range(len(nums)):
            total += nums[i]

        if total - nums[0] == 0:
            return 0

        for i in range(1, len(nums)):
            left += nums[i-1]
            right = total - nums[i] - left

            if left == right:
                return i

        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna