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

        stack = []
        s = head
        while s.next:
            stack.append(s.next)
            s = s.next

        s = head
        n = 0
        while stack:
            if n % 2 == 0:
                one = stack.pop()
            else:
                one = stack.pop(0)
            one.next = None
            s.next = one
            s = s.next
            n += 1


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