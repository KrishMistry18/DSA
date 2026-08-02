class Solution(object):
    def countRatioSubarrays(self, nums, a, b):
        ans = 0
        n = len(nums)

        for i in range(n):
            even = 0
            odd = 0

            for j in range(i, n):

                if nums[j] % 2 == 0:
                    even += 1
                else:
                    odd += 1

                if odd > 0 and even * b <= odd * a:
                    ans += 1

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna