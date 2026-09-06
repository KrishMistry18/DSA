import heapq

class Solution:
    def kthSmallest(self, arr, k):
        heap = []

        for num in arr:
            heapq.heappush(heap, -num)

            if len(heap) > k:
                heapq.heappop(heap)

        return -heap[0]



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna