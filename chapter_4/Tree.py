

class Node:

    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

class Tree:

    def insert_node(self, node, data):
        if not node:
            return Node(data)
        # insert left
        elif data < node.data:
            node.left  = self.insert_node(node.left, data)
        # insert right
        elif data > node.data:
            node.right = self.insert_node(node.right, data)

        return node

    def pre_order(self, root):
        if root:
            print(root.data)
            self.pre_order(root.left)
            self.pre_order(root.right)

    def in_order(self, root):
        if root:
            self.in_order(root.left)
            print(root.data)
            self.in_order(root.right)

    def post_order(self, root):
        if root:
            self.post_order(root.left)
            self.post_order(root.right)
            print(root.data)


if __name__== "__main__":

    T = Tree()

    Root = T.insert_node(None, 1)
    T.insert_node(Root, 0)
    T.insert_node(Root, 2)

    T.pre_order(Root)
    print()
    T.in_order(Root)
    print()
    T.post_order(Root)
