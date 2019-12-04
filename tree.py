class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.status = 0

    def LTR(self):
        if self.left:
            self.left.LTR()

        print(self.val)

        if self.right:
            self.right.LTR()

    def walk(self):
        stack = [self]

        while len(stack):
            node = stack.pop()
            if node.status == 1:
                print(node.val)
            else:
                if node.right:
                    stack.append(node.right)

                node.status = 1
                stack.append(node)

                if node.left:
                    stack.append(node.left)




root = Node(4)
root.left = Node(2)
root.left.left = Node(1)
root.left.right = Node(3)
root.right = Node(6)
root.right.left = Node(5)
root.right.right = Node(7)


# root.LTR()

root.walk()
