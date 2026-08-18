class Solution(object):
    def firstUniqChar(self, s):
        n = len(s)
        f = {}

        for i in range(n):
            f[s[i]] = f.get(s[i], 0) + 1

        for i in range(n):
            if f[s[i]] == 1:
                return i

        return -1 


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna