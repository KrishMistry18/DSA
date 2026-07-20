class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums)
        if n <= 2:
            return n
        i = 1
        count = 2
        j = 2
        while j < n:
            if nums[j] != nums[i - 1]:
                nums[i + 1] = nums[j]
                i += 1
                count += 1
            j += 1
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna