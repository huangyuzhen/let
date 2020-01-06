# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        pa = headA
        pb = headB

        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA

        return pa


def initData():
    a0 = ListNode(4)
    a1 = ListNode(1)
    a2 = ListNode(8)
    a3 = ListNode(4)
    a4 = ListNode(5)


    a0.next = a1
    a1.next = a2
    a2.next = a3
    a3.next = a4

    b0 = ListNode(5)
    b1 = ListNode(0)
    b2 = ListNode(1)

    b0.next = b1
    b1.next = b2
    b2.next = a2

    return a0, b0

headA, headB = initData()
sol = Solution()
x = sol.getIntersectionNode(headA, headB)
if x:
    print(x.val)
else:
    print(None)
