'''
递归反转整个链表
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def reverse(head):
    if not head.next: return head
    tail = head.next
    head.next = None
    last = reverse(tail)
    tail.next = head

    return last



link = None
for i in range(5, 0, -1):
    a = ListNode(i)
    a.next = link
    link = a
origin = link

r = reverse(origin)
link = r
while link:
    print(link.val)
    link = link.next