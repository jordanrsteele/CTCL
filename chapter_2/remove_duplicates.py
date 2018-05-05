from llist import sllist

def remove_duplicates(lst):

    head = lst.first

    if head == None:
        return lst

    start = head

    my_set = set()
    curr = head
    while curr != None:
        print(curr)
        print(my_set)
        # remove from list
        if curr.value in  my_set:
            pointer = curr.next
            lst.remove(curr)
            curr = pointer

        else:
            my_set.add(curr.value)
            curr = curr.next

    return lst

L = sllist()

L.append(1)
L.append(2)
L.append(1)
L.append(2)
L.append(5)

new_list = remove_duplicates(L)
print(new_list)
