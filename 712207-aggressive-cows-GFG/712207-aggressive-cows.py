class Solution:
    def aggressiveCows(self, arr, k):
        arr.sort()

        low = 1
        high = arr[-1] - arr[0]
        ans = 0

        def canPlace(distance):
            cows = 1
            last = arr[0]

            for i in range(1, len(arr)):
                if arr[i] - last >= distance:
                    cows += 1
                    last = arr[i]   

                    if cows == k:
                        return True

            return False

        while low <= high:
            mid = (low + high) // 2

            if canPlace(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna