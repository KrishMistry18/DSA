import heapq

class Solution(object):
    def mergeKLists(self, lists):
        pq = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(pq, (lists[i].val, i, lists[i]))

        dummy = ListNode(0)
        curr = dummy

        while pq:

            value, i, node = heapq.heappop(pq)
            curr.next = node
            curr = curr.next
            
            if node.next:
                heapq.heappush(
                    pq,
                    (node.next.val, i, node.next)
                )

        return dummy.next

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna