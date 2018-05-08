

class MyQueue:

    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()


    def enque(self, val):
        self.stack1.append(val)
        return val

    def deque(self):
        if not self.stack1:
            return None

        while self.stack1:
            self.stack2.append(self.stack1.pop())

        val = self.stack2.pop()

        while self.stack2:
            self.stack1.append(self.stack2.pop())

        return val

    def peak(self):

        if not self.stack1:
            return None

        while self.stack1:
            self.stack2.append(self.stack2.pop())

        val = self.stack2[len(self.stack2) - 1]

        while self.stack2:
            self.stack.append(self.stack2.pop())

        return val

    def print_stack(self):
        print(self.stack1)

"""
Q = MyQueue()

for i in range(10):
    Q.enque(i)

print(Q.stack1)

for i in range(10):
    print(Q.deque())
"""
