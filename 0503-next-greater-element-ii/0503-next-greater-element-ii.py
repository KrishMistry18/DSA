class Solution(object):
    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):
            index = i % n

            while stack and stack[-1] <= nums[index]:
                stack.pop()

            if i < n:
                if stack:
                    res[index] = stack[-1]

            stack.append(nums[index])

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna