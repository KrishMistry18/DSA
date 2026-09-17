import heapq

class Solution(object):
    def leastInterval(self, tasks, n):
        freq = {}

        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        pq = []

        for task in freq:
            heapq.heappush(pq, -freq[task])

        time = 0
        q = []

        while pq or q:
            time += 1

            if pq:
                count = heapq.heappop(pq)
                count += 1

                if count != 0:
                    q.append((count, time + n))

            if q and q[0][1] == time:
                heapq.heappush(pq, q.pop(0)[0])

        return time

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna