class Solution(object):
    def lengthOfLongestSubstring(self, s):
        low = 0
        high = 0
        k = 0
        length = 0
        f = {}
        res = 0

        for high in range(len(s)):
            f[s[high]] = f.get(s[high],0) + 1

            while f[s[high]] > 1:
                f[s[low]] = f.get(s[low],0) - 1
                
                if f[s[low]] == 0:
                    del f[s[low]]

                low += 1
                
            length = high - low + 1
            res = max(length,res)

        return res





        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna