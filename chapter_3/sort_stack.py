from random import *


def sort_stack(stack):
    temp_stack = []

    while stack:
        temp = stack.pop()

        # if top of temp stack is greater than temp
        while temp_stack and temp_stack[len(temp_stack)-1] > temp:
            stack.append(temp_stack.pop())

        # add temp to temp_stack
        temp_stack.append(temp)

    return temp_stack

Q = list()

for i in range(10):
    num = randint(0,9)
    Q.append(num)

print(Q)

Q = sort_stack(Q)

print(Q)
