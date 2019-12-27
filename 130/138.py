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

        s = head
        t = root

        index = 0
        s.index = index
        dic[index] = t

        while s.next:
            s = s.next
            t.next = Node(s.val)
            t = t.next
            index += 1
            s.index = index
            dic[index] = t


        s = head
        t = root
        while s:
            if s.random:
                t.random = dic[s.random.index]
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
print(x)

t = x
while t:
    print(t.val)
    if t.random: print("random:", t.random.val)
    t = t.next

