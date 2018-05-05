from singleLinkedList import singleLinkedList


def sum_lists(l1, l2):
    sum = 0
    num1 = 0
    num2 = 0
    num1_list = list()
    num2_list = list()
    curr1 = l1.head
    curr2 = l2.head

    if not l1.head and not l2.head:
        print("sum: " + sum)
        return sum

    # add values to list, index corresponds to power of 10
    while curr1:
        num1_list.append(curr1.data)
        curr1 = curr1.next

    while curr2:
        num2_list.append(curr2.data)
        curr2 = curr2.next

    for i in range(len(num1_list) - 1, -1, -1):
        num1 = num1 + num1_list[i]*(10**i)

    for i in range(len(num2_list) - 1, -1, -1):
        num2 = num2 + num2_list[i]*(10**i)

    sum = num1 + num2
    return sum

if __name__== "__main__":

    L1 = singleLinkedList()
    L2 = singleLinkedList()

    L1.add(6)
    L1.add(1)
    L1.add(7)

    L2.add(2)
    L2.add(9)
    L2.add(5)


    L1.print_list()
    L2.print_list()
    sum = sum_lists(L1, L2)
    print(sum)
