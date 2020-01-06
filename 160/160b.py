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
        if not headA or not headB: return None

        pa = headA
        pb = headB

        while pa and pb:
            if pa == pb:
                return pa
            pa = pa.next
            pb = pb.next

        if not pa and not pb:
            return None

        if not pa:
            pa = headB
            while pa:
                if pa == pb:
                    return pa
                pa = pa.next
                pb = pb.next
                if pb == None:
                    pb = headA

        elif not pb:
            pb = headA
            while pb:
                if pa == pb:
                    return pa
                pb = pb.next
                pa = pa.next
                if pa == None:
                    pa = headB


        return None


def initData():
    a0 = ListNode(1)
    a1 = ListNode(2)
    a2 = ListNode(3)
    a3 = ListNode(4)
    a4 = ListNode(5)


    a0.next = a1
    a1.next = a2
    a2.next = a3
    a3.next = a4

    b0 = ListNode(6)
    b1 = ListNode(7)
    b2 = ListNode(8)

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
