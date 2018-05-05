from singleLinkedList import singleLinkedList


def delete_middle_node(node):

    # make pointer to next node
    node1 = node.next
    node.data = node.next.data
    node.next = node.next.next

    # remove deleted node's references
    node1.data = None
    node1.next = None



L = singleLinkedList()
for i in range(0, 11):
    L.add(i)

middleNode = L.get_node(5)


L.print_list()



delete_middle_node(middleNode)
print()
L.print_list()
