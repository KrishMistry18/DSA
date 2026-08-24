class Solution(object):
    def findMin(self, nums):
        n = len(nums)
        low = 0
        high = n - 1
        res = -1

        while low <= high:
            guess = (low + high)//2

            if nums[guess] > nums[-1]:
                low = guess + 1

            else:
                res = guess
                high = guess - 1

        return nums[res]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna