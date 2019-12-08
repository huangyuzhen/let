# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findMid(self, head):
        prev = None
        p_1x = head
        p_2x = head

        while p_2x and p_2x.next:
            prev = p_1x
            p_1x = p_1x.next
            p_2x = p_2x.next.next

        if prev: prev.next = None
        return p_1x

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        if not head: return None

        mid = self.findMid(head)
        node = TreeNode(mid.val)

        if head == mid: return node

        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)

        return node



def initData():
    nums = [-10,-3,0,5,9]
    head = None
    for number in nums[::-1]:
        node = ListNode(number)
        node.next = head
        head = node
    return head

def f(root):
    return f(root.left) + [root.val] + f(root.right) if root else []

head = initData()



s = Solution()
x = s.sortedListToBST(head)
print(f(x))
