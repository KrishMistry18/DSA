class Solution(object):
    def countValidPrefixes(self, s):
        count0 = 0
        count1 = 0
        ans = 0

        for ch in s:
            if ch == '0':
                count0 += 1
            else:
                count1 += 1

            if abs(count0 - count1) <= 1:
                ans += 1

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna