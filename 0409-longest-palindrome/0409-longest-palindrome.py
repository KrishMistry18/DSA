class Solution(object):
    def longestPalindrome(self, s):
        f = {}
        res = 0
        odd = False

        for i in range(len(s)):
            f[s[i]] = f.get(s[i], 0) + 1

        for char in f:
            if f[char] % 2 != 0:
                res += f[char] - 1
                odd = True

            else:
                res += f[char]
            
        if odd:
            res += 1

        return res
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna