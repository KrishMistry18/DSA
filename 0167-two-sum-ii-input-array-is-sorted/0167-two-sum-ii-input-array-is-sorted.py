class Solution(object):
    def twoSum(self, numbers, target):
        i=0
        j=len(numbers)-1
        while i<j:
            total=numbers[i]+numbers[j]
            while total==target:
                return [i+1,j+1]
            if total<target:
                i+=1
            else:
                j-=1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna