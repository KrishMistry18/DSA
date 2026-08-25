class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums) - 1

        while low <= high:
            guess = (low + high) // 2

            if nums[guess] == target:
                return guess

            if nums[low] <= nums[guess]:
                if nums[low] <= target < nums[guess]:
                    high = guess - 1
                else:
                    low = guess + 1

            else:
                if nums[guess] < target <= nums[high]:
                    low = guess + 1
                else:
                    high = guess - 1

        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna