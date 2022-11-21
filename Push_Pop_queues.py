#deque is used as it is faster than list when both ends are considered

from collections import deque


class Stack:

    def __init__(self):

        # Two inbuilt queues are made the moment the class is called
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):

        # Push x first in empty q2
        self.q2.append(x)

        # Push all the remaining
        # elements in q1 to q2.
        while (self.q1):
            self.q2.append(self.q1.popleft())

        # swap the names of two queues
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.q1:
            self.q1.popleft()

    def top(self):
        if (self.q1):
            return self.q1[0]
        return None

    def size(self):
        return len(self.q1)


if __name__ == '__main__':
    s = Stack()
    user_input = 3
    while user_input!=5:
        user_input = int(input("\nEnter the value \n1 for push\n2 for Pop\n3 for size\n4 to see the top element\n5 to quit\n"))
        if user_input==1:
            value = int(input("Enter value to push : "))
            s.push(value)
        elif user_input == 2:
            if s.size() == 0:
                print("Queue is empty")
                break
            s.pop()
        elif user_input == 3:
            print("current size: ", s.size())
        elif user_input == 4:
            print("Top element is: " , s.top())
        elif user_input == 5:
            break
        else:
            print("Wrong option")
            break

    print("current size of queue is: ", s.size())