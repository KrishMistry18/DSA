class Solution(object):
    def removeElement(self, nums, val):
        low = 0
        high = len(nums) - 1

        while low <= high:
            if nums[high] == val:
                high -= 1

            elif nums[low] == val:
                nums[low], nums[high] = nums[high], nums[low]
                low += 1
                high -= 1

            else:
                low += 1

        return high + 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna