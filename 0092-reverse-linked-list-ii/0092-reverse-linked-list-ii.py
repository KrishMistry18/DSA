class Solution(object):
    def reverseBetween(self, head, left, right):
        if left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        for i in range(left - 1):
            prev = prev.next

        curr = prev.next

        for i in range(right - left):
            next = curr.next
            curr.next = next.next
            next.next = prev.next
            prev.next = next

        return dummy.next

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna