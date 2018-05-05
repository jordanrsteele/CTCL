from singleLinkedList import singleLinkedList

def partition(lst, val):

    if not lst.head:
        return None

    less_than = singleLinkedList()
    greater_or_equal = singleLinkedList()

    curr = lst.head

    while curr:
        if curr.data < val:
            less_than.add(curr.data)
        else:
            greater_or_equal.add(curr.data)

        curr = curr.next

    if less_than.head:
        lst.head = less_than.head
        lst.tail = less_than.tail

    if greater_or_equal.head:
        lst.tail.next = greater_or_equal.head
        lst.tail = greater_or_equal.tail

    return lst



L = singleLinkedList()

L.add(1)
L.add(5)
L.add(2)
L.add(3)
L.add(0)

L.print_list()

partition(L, 2)

L.print_list()
