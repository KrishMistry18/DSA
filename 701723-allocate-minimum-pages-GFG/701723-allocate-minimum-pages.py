class Solution:
    def findPages(self, arr, k):
        n = len(arr)

    # More students than books
        if k > n:
            return -1

        low = max(arr)
        high = sum(arr)
        ans = high

        def canAllocate(limit):
            students = 1
            pages = 0

            for book in arr:
                if pages + book <= limit:
                    pages += book
                else:
                    students += 1
                    pages = book

                    if students > k:
                        return False

            return True

        while low <= high:
            mid = (low + high) // 2

            if canAllocate(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna