from singleLinkedList import singleLinkedList
from collections import OrderedDict
# a -> b -> c -> d -> e
# x -> y ->^

# check if intersection by reference
def is_intersection(l1, l2):
    long_list = l1
    short_list = l2
    curr1 = l1.head
    curr2 = l2.head

    if not curr1 or not curr2:
        return None

    # get length of lists
    l1_len = 0
    l2_len = 0
    while curr1:
        l1_len = l1_len + 1
        curr1 = curr1.next

    while curr1:
        l2_len = l2_len + 1
        curr2 = curr2.next

    diff = l1_len - l2_len

    # only iterate through longer list to start
    if diff >= 0:
        long_list = l1
        short_list = l2
    else:
        long_list = l2
        short_list = l1
        # make diff positive
        diff = diff * (-1)

    # reset pointers
    curr1 = long_list.head
    curr2 = short_list.head

    count = 0

    while curr1 and count < diff:
        curr = curr1.next
        count = count + 1

    # list should be at the same place now, iterate
    while curr1:
        if curr1 == curr2:
            return curr1

        curr1 = curr1.next
        curr2 = curr2.next

    return None

def is_intersection_hash(l1, l2):
    address_list = list()
    curr1 = l1.head
    curr2 = l2.head

    while curr1:
        address_list.append(id(curr1))
        curr1 = curr1.next

    while curr2:
        if id(curr2) in address_list:
            return curr2

        curr2 = curr2.next

    return None

if __name__== "__main__":
    L1 = singleLinkedList()
    L2 = singleLinkedList()

    # create lists
    L1.add(1)
    L1.add(2)
    node = L1.add(12)
    L1.add(4)

    L2.add(5)
    L2.add(6)
    L2.add_node(node)


    print(is_intersection(L1, L2).data)

    print(is_intersection_hash(L1, L2).data)
