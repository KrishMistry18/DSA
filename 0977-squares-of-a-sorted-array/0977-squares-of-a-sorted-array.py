class Solution(object):
    def sortedSquares(self, arr):
        a = []
        b = [] 
        n = len(arr)
        res = []
        k = 0
        l = 0

        for num in arr:
            if num < 0:
                a.append(num)
            else:
                b.append(num) 
    
        if len(a) == 0:
            for q in range(n):
                arr[q] = arr[q]*arr[q]
            return arr
        
        if len(b) == 0:
            for q in range(n):
                arr[q] = arr[q]*arr[q]
            arr.reverse()
            return arr 
    
        for i in range (len(a)):
            a[i] = a[i]*a[i]
        a.reverse()
    
        for i in range (len(b)):
            b[i] =b[i]*b[i]
    
        while (k < len(a) and l < len(b)):
            if a[k] < b[l]:
                res.append(a[k])
                k += 1
            else:
                res.append(b[l])
                l += 1
        while k < len(a):
            res.append(a[k])
            k += 1

        while l < len(b):
            res.append(b[l])
            l += 1

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna