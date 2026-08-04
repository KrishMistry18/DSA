class Solution(object):
    def frequencySort(self, s):
        f= {}
        maxi = 0
        str =[]

        for i in range(len(s)):
            f[s[i]] = f.get(s[i],0) + 1

        count = len(f)

        while count > 0:
            maxi = max(f.values())

            for ch in f:
                if f[ch] == maxi:
                    while maxi >0:
                        str.append(ch)
                        maxi -=1
                    del f[ch]
                    break
            count -=1
        return "".join(str)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna