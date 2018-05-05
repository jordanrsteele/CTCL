from llist import sllist



def kth_to_last(lst, k):
    node1 = node2 = lst.first

    if node1 == None:
        return None

    count = 0
    # make nodes k nodes apart
    while node2 != None and count <= k:
        node2 = node2.next
        count = count + 1
        print(count)

    while node2 != None:
        node1 = node1.next
        node2 = node2.next

    # create a new list to return
    k_list = sllist()
    while node1 != None:
        k_list.append(node1)
        node1 = node1.next

    return k_list

L = sllist()

for i in range(0, 5):
    L.append(i)

print(L)

new_list = kth_to_last(L, 1)

print(new_list)
