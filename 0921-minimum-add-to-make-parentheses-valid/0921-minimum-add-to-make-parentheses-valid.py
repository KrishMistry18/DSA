class Solution(object):
    def minAddToMakeValid(self, s):
        open = 0
        ans = 0

        for ch in s:
            if ch == '(':
                open += 1

            else:  # ')'
                if open > 0:
                    open -= 1
                else:
                    ans += 1

        return ans + open

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna