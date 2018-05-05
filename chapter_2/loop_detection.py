from singleLinkedList import singleLinkedList

# Floyds Cycle detection algorithm d = x + y, loop = y + z
def is_loop(lst):
    curr1 = lst.head
    curr2 = lst.head

    if not curr1:
        return None

    while curr2 and curr2.next:
        curr1 = curr1.next
        curr2 = curr2.next.next

        if curr1 == curr2:
            break

    curr1 = lst.head

    while curr1:
        if curr1 == curr2:
            return curr1

        curr1 = curr1.next
        curr2 = curr2.next

    return None

if __name__== "__main__":

    L1 = singleLinkedList()

    # create lists
    L1.add(1)
    L1.add(2)
    node = L1.add(12)
    L1.add(4)
    L1.add(5)
    L1.add_node(node)

    print("******")
    print(is_loop(L1).data)
    print("******")
