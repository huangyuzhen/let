class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def LTR(self, result):
        if self.left:
            self.left.LTR(result)
        result.append(self.val)
        if self.right:
            self.right.LTR(result)

    def TLR(self, result):
        result.append(self.val)
        if self.left:
            self.left.TLR(result)
        if self.right:
            self.right.TLR(result)

    def LRT(self, result):
        if self.left:
            self.left.LRT(result)
        if self.right:
            self.right.LRT(result)
        result.append(self.val)

    # 使用栈实现的LTR
    def walk(self):
        result = []
        stack = [self]

        while len(stack):
            node = stack.pop()
            if hasattr(node, 'status') and node.status == 1:
                result.append(node.val)
            else:
                if node.right:
                    stack.append(node.right)

                node.status = 1
                stack.append(node)

                if node.left:
                    stack.append(node.left)

        return result

    def walk2(self):
        result = []
        stack = []
        cur = self

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right

        return result



root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)


# result = []
# root.TLR(result)
# print(result)

x = root.walk2()
print(x)
