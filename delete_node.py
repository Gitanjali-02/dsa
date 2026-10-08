class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new_node

    def del_node(self, value):
        prev = None
        temp = self.head

        # Empty list
        if temp is None:
            print("List is empty")
            return

        # Delete first node
        if temp.data == value:
            self.head = self.head.next
            return

        # Search
        while temp:
            if temp.data == value:
                break

            prev = temp
            temp = temp.next

        # Not found
        if temp is None:
            print("Value is not there in the list")
            return

        # Delete node
        prev.next = temp.next
        temp = None

    def print(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next


list = LinkedList()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))

list.print()

print("____")

list.del_node(55)

list.print()