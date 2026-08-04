class Solution(object):
    def subarraySum(self, nums, k):
        f = {}
        prefix_sum = 0
        f[0] = 1
        count = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            ques = prefix_sum - k
            count += f.get(ques, 0)

            f[prefix_sum] = f.get(prefix_sum, 0) + 1

        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna