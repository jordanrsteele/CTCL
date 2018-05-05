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
for i in range(0, 5):
    L.add(i)

middleNode = L.add(5)

for i in range(6, 11):
    L.add(i)

L.print_list()



delete_middle_node(middleNode)
print()
L.print_list()
