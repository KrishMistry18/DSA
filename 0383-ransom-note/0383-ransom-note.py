class Solution(object):
    def canConstruct(self, ransom, magazine):
        have = {}
        need = {}

        for i in range(len(ransom)):
            need[ransom[i]] = need.get(ransom[i], 0) + 1

        for i in range(len(magazine)):
            have[magazine[i]] = have.get(magazine[i], 0) + 1

        for char in need:
            if char not in have:
                return False
            
            if have[char] < need[char]:
                return False
        
        return True
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna