# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """

        if not head: return

        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        s2 = slow.next
        s1 = head
        slow.next = None

        stack = []
        s = s2
        while s:
            stack.append(s)
            s = s.next

        s = s1
        while stack:
            a = stack.pop()
            a.next = s.next
            s.next = a
            s = a.next




def initData():
    a0 = ListNode(1)

    a1 = ListNode(2)
    a0.next = a1

    a2 = ListNode(3)
    a1.next = a2

    a3 = ListNode(4)
    a2.next = a3

    a4 = ListNode(5)
    a3.next = a4

    return a0


head = initData()
sol = Solution()
sol.reorderList(head)

s = head
while s:
    print( s.val)
    s = s.next