# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head: return None

        x = head.next
        head.next = None

        while x:
            tmp = x.next
            x.next = None

            # head = self.insert(head, x)
            if head.val >= x.val:
                x.next = head
                head = x
            else:
                y = head
                while y.next and y.next.val < x.val:
                    y = y.next
                x.next = y.next
                y.next = x

            x = tmp

        return head



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
x = sol.insertionSortList(head)

while x:
    print("result:", x.val)
    x = x.next
