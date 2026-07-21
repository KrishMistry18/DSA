class Solution(object):
    def characterReplacement(self, s, k):
        low = 0
        high = 0
        n = len(s)
        f = {}
        res = 0

        for high in range (n):
            f[s[high]] = f.get(s[high],0) + 1
            length = high - low + 1
            max_count = max(f.values())
            diff = length -  max_count

            while diff > k:
                f[s[low]] = f.get(s[low],0) - 1

                if f[s[low]] == 0:
                    del f[s[low]]
             
                low += 1
                length = high - low + 1
                max_count = max(f.values())
                diff = length -  max_count
            
                if f: # prevent max() on empty dict
                    max_count = max(f.values())
                else:
                    max_count = 0
                diff = length - max_count

            res = max(length,res)

        return res

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna