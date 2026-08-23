class Solution(object):
    def searchRange(self, nums, target):
        n = len(nums)
        result = [-1, -1]
        
        low = 0
        high = n - 1

        while low <= high:
            guess = (low + high) // 2

            if nums[guess] < target:
                low = guess + 1

            elif nums[guess] > target:
                high = guess - 1

            else:
                result[0] = guess
                high = guess - 1

        low = 0
        high = n - 1

        while low <= high:
            guess = (low + high) // 2

            if nums[guess] < target:
                low = guess + 1

            elif nums[guess] > target:
                high = guess - 1

            else:
                result[1] = guess
                low = guess + 1

        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna