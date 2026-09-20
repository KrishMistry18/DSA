class Solution(object):
    def reverseDegree(self, s):
        ans = 0

        for i in range(len(s)):
            value = 26 - (ord(s[i]) - ord('a'))
            ans += value * (i + 1)

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna