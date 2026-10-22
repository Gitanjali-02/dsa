
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isempty():
            print("Stack is empty")
        else:
            temp = self.top
            print("\nPopped element:", temp.data)
            self.top = self.top.next
            temp.next = None

    def print_stack(self):
        if self.isempty():
            print("Stack is empty")
        else:
            print("Stack contains:")
            temp = self.top
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

    def reverse(self):
        st1 = Stack()
        temp = self.top

        while temp:
            st1.push(Node(temp.data))
            temp = temp.next

        self.top = st1.top


obj = Stack()

obj.push(Node(1))
obj.push(Node(2))
obj.push(Node(3))
obj.push(Node(4))

obj.print_stack()

obj.pop()

obj.reverse()

obj.print_stack()
