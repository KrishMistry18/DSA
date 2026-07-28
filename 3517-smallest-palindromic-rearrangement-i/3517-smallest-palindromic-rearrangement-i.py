class Solution(object):
    def smallestPalindrome(self, s):
        n = len(s)
        res = ""
        mid = ""
        f = {}

        for ch in s:
            f[ch] = f.get(ch, 0) + 1

        for ch in sorted(f):
            if f[ch] % 2 == 0:
                res += ch * (f[ch] // 2)
            
            elif f[ch] % 2 == 1:
                res += ch * (f[ch] // 2)
                mid = ch

        return res + mid + res[::-1]

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna