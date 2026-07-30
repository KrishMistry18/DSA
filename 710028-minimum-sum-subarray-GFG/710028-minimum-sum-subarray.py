class Solution:
    def smallestSumSubarray(self, A, N):
        #Your code here
        i = 0
        best = A[i]
        ans = A[i]

        for i in range (1,N):
            v1 = best + A[i]
            v2 = A[i]
            
            best = min(v1,v2)
            ans = min(ans,best)
            
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna