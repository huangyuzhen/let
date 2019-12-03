'''
反转链表前 N 个节点
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseNt(self, head, n):
        tail = head.next
        head.next = None
        if not tail or n == 1:
            self.suffix = tail
            return head
        last = self.reverseNt(tail, n-1)
        tail.next = head
        return last

    def reverseN(self, head, n):
        last = self.reverseNt(head, n)
        head.next = self.suffix

        return last


link = None
for i in range(5, 0, -1):
    a = ListNode(i)
    a.next = link
    link = a
origin = link

solution = Solution()
r = solution.reverseN(origin, 2)
link = r
while link:
    print(link.val)
    link = link.next