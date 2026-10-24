class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Lueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):
        if self.rear:
            self.rear.next = new_node
            self.rear = new_node
        else:
            self.front = self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front
        print("\nDeleted node:", temp.data)

        self.front = self.front.next
        temp = None

        if self.front is None:
            self.rear = None

    def print(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


que = Lueue()

que.enqueue(Node(1))
que.enqueue(Node(2))
que.enqueue(Node(3))
que.enqueue(Node(4))

print("Queue elements:")
que.print()

que.dequeue()

print("\nQueue after deletion:")
que.print()