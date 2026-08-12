class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        n = len(nums2)
        stack = []
        greater = {}

        for i in range(n - 1, -1, -1):

            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if stack:
                greater[nums2[i]] = stack[-1]
            else:
                greater[nums2[i]] = -1

            stack.append(nums2[i])

        res = []

        for num in nums1:
            res.append(greater[num])

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna