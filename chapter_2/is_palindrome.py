from singleLinkedList import singleLinkedList

def is_palindrome(lst):
    stack = []

    if not lst.head:
        return False

    node1 = lst.head
    node2 = lst.head

    while node2 and node2.next:
        stack.append(node1.data)

        node1 = node1.next
        node2 = node2.next.next

    # must be odd
    if node2:
        node1 = node1.next

    while node1:
        val = stack.pop()
        if val != node1.data:
            return False

        node1 = node1.next

    return True

if __name__== "__main__":

    L = singleLinkedList()

    L.add("r")
    L.add("a")
    L.add("c")
    L.add("e")
    L.add("c")
    L.add("a")
    L.add("r")

    L.print_list()

    print(is_palindrome(L))
