class Solution(object):
    def search(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            guess = (low + high) // 2

            if nums[guess] == target:
                return guess

            elif nums[guess] < target:
                low = guess + 1

            else:
                high = guess - 1

        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna