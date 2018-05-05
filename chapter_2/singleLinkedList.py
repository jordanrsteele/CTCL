

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class singleLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        new_node = Node()
        new_node.data = data

        # list ist empty
        if self.head == None:
            self.head = self.tail = new_node
        # add to end of list
        else:
            self.tail.next = new_node
            self.tail = new_node

        return self.tail

    def add_node(self, node):
        # list ist empty
        if self.head == None:
            self.head = self.tail = node

        else:
            self.tail.next = node
            self.tail = node

        return self.tail

    def get_node(self, val):
        curr = self.head
        while curr:
            if curr.data == val:
                return curr
            curr = curr.next

        return None

    def print_list(lst):
        curr = lst.head
        lst = list()
        while curr:
            lst.append(curr.data)
            curr = curr.next

        print(lst)
