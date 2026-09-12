import heapq

class Solution(object):
    def findMaximizedCapital(self, k, w, profits, capital):

        n = len(profits)
        proj = []

        for i in range(n):
            proj.append((capital[i], profits[i]))

        proj.sort()
        pq = []
        idx = 0

        while k > 0:
            while idx < n and proj[idx][0] <= w:
                heapq.heappush(pq, -proj[idx][1])
                idx += 1

            if not pq:
                return w

            w += -heapq.heappop(pq)
            k -= 1

        return w

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna