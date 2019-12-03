# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n: return head

        prefix = ListNode(0)
        tail = prefix

        cur = head
        index = 0
        while cur:
            tmp = cur.next
            index += 1
            if index < m or index > n:
                tail.next = cur
                tail = tail.next
                cur = cur.next
            elif index == m:
                left = cur
                right = cur
                cur.next = None
            elif index == n:
                cur.next = left
                tail.next = cur
                tail = right
            else: # m < index < n
                cur.next = left
                left = cur

            cur = tmp

        return prefix.next




# linkList = None
# for i in range(5, 0, -1):
#     a = ListNode(i)
#     a.next = linkList
#     linkList = a

# c = linkList
# while c:
#     print(c.val)
#     c = c.next

linkList = ListNode(3)
linkList.next = ListNode(5)

m = 1
n = 2

solution = Solution()
x = solution.reverseBetween(linkList, m, n)

c = x
while c:
    print(c.val)
    c = c.next
