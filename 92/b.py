'''
反转链表前 N 个节点
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseN(head, n):
    def reverseNt(head, N, n):
        tail = head.next
        head.next = None
        if n == 1: return head, tail
        last, part = reverseNt(tail, N, n-1)
        tail.next = head
        return last, part

    last, part = reverseNt(head, n, n)
    head.next = part
    return last


link = None
for i in range(5, 0, -1):
    a = ListNode(i)
    a.next = link
    link = a
origin = link

r = reverseN(origin, 2)
link = r
while link:
    print(link.val)
    link = link.next