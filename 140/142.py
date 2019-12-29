# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        fast = slow = head
        found = None

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                found = head
                break

        if found:
            while found != slow:
                found = found.next
                slow  = slow.next

        return found



def initData():
    a0 = ListNode(3)
    a1 = ListNode(2)
    a2 = ListNode(0)
    a3 = ListNode(-4)


    a0.next = a1
    a1.next = a2
    a2.next = a3
    a3.next = a1

    return a0


head = initData()
sol = Solution()
x = sol.detectCycle(head)
if x:
    print(x.val)
