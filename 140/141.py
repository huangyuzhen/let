# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        s = head
        while s:
            print(s.val)
            s = s.next


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
x = sol.hasCycle(head)
print(x)
