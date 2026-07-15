class Solution:
    def longestKSubstr(self, s, k):
        low = 0
        high = 0
        length = 0
        res = -1
        n = len(s)
        f = {}
        
        for high in range (n):
            f[s[high]] = f.get(s[high],0) + 1
            
            while len(f) > k:
                f[s[low]] = f.get(s[low],0) - 1
                
                if f[s[low]] == 0:
                    del f[s[low]]   
                
                low += 1
                    
            if len(f) == k:
                length = high - low + 1
                res = max(length,res)
                
        return res
                
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna