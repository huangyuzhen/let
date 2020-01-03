# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def merge(self, L1, L2):
        dummyHead = ListNode(0)
        p = dummyHead

        while L1 and L2:
            if L1.val >= L2.val:
                L1, L2 = L2, L1
            p.next = L1
            p = p.next
            L1 = L1.next

        if L1:
            p.next = L1
        else:
            p.next = L2

        return dummyHead.next

    def cut(self, head, n):
        p = head
        n -= 1
        while n and p:
            p = p.next
            n -= 1

        if not p: return None

        tmp = p.next
        p.next = None

        return tmp


    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = head

        p = head
        length = 0
        while p:
            length += 1
            p = p.next

        size = 1
        while size < length:
            cur = dummyHead.next
            tail = dummyHead

            while cur:
                left = cur
                right = self.cut(left, size)
                cur = self.cut(right, size)

                tail.next = self.merge(left, right)
                while tail.next:
                    tail= tail.next

            size = size << 1

        return dummyHead.next




def initData():
    a0 = ListNode(4)

    a1 = ListNode(2)
    a0.next = a1

    a2 = ListNode(1)
    a1.next = a2

    a3 = ListNode(3)
    a2.next = a3

    return a0

head = initData()
sol = Solution()
x = sol.sortList(head)

while x:
    print("result:", x.val)
    x = x.next
