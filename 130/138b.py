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

        dic = {}
        root = Node(head.val)
        dic[head] = root

        s = head
        t = root
        while s.next:
            s = s.next
            t.next = Node(s.val)
            t = t.next
            dic[s] = t

        s = head
        t = root
        while s:
            if s.random:
                t.random = dic[s.random]
            s = s.next
            t = t.next


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

