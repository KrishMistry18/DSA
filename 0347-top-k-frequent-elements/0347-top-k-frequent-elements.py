import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        pq = []

        for element, frequency in freq.items():
            curr = (frequency, element)
            heapq.heappush(pq, curr)

            if len(pq) > k:
                heapq.heappop(pq)

        res = []

        while pq:
            frequency, element = heapq.heappop(pq)
            res.append(element)

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna