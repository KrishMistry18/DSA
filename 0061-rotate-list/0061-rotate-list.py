# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head == None:
            return None
        
        last = head
        n = 1
        
        while last.next != None:
            n += 1
            last = last.next

        k = k % n
        if k == 0:
            return head

        t = head
        count = 1

        while t!= None:
            if count == (n - k):
                break
            count += 1
            t = t.next

        last.next = head
        res = t.next
        t.next = None

        return res


        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna