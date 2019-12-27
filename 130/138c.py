"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        if not head: return None

        s = head
        while s:
            t = Node(s.val)
            t.next = s.next
            s.next = t
            s = t.next

        s = head
        while s:
            t = s.next
            if s.random:
                t.random = s.random.next
            s = t.next

        root = head.next
        s = head
        while s:
            t = s.next
            s.next = t.next

            s = t.next
            if s:
                t.next = s.next

        return root


def initData():
    a = Node(3)
    b = Node(3)
    c = Node(3)

    a.next = b
    b.next = c
    b.random = a

    return a

head = initData()
sol = Solution()
x = sol.copyRandomList(head)

t = x
while t:
    print(t.val)
    if t.random: print("random:", t.random.val)
    t = t.next

