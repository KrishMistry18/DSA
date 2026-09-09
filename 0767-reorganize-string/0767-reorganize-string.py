import heapq

class Solution(object):
    def reorganizeString(self, s):

        count = {}

        for ch in s:
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

        pq = []

        for ch in count:
            heapq.heappush(pq, (-count[ch], ch))

        res = []

        while pq:
            p = heapq.heappop(pq)

            if not res or res[-1] != p[1]:
                res.append(p[1])
                p = (p[0] + 1, p[1])

                if p[0] < 0:
                    heapq.heappush(pq, p)

            else:
                if not pq:
                    return ""

                p2 = heapq.heappop(pq)
                res.append(p2[1])
                p2 = (p2[0] + 1, p2[1])

                if p2[0] < 0:
                    heapq.heappush(pq, p2)

                heapq.heappush(pq, p)

        return "".join(res)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna