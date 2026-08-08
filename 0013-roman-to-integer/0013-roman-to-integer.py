class Solution(object):
    def romanToInt(self, s):
        f = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        ans = 0
        for i in range(len(s)):
            if i + 1 < len(s) and f[s[i]] < f[s[i + 1]]:
                ans -= f[s[i]]
            else:
                ans += f[s[i]]
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna