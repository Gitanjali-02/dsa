
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, data, position):
        new_node = Node(data)

        # Insert at first position
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        count = 1

        # Move to previous node
        while temp is not None and count < position - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid Position")
            return

        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# Main program
ll = LinkedList()

ll.insert_at_position(10, 1)
ll.insert_at_position(20, 2)
ll.insert_at_position(30, 3)

print("Before insertion:")
ll.display()

ll.insert_at_position(25, 3)

print("After insertion:")
ll.display()
