
class Node:
    def __init__(self, value):
        self.prev = None
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        temp = self.head

        if temp:
            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp
        else:
            self.head = new_node

    def occurence(self, num):
        temp = self.head
        count = 0

        while temp:
            if temp.data == num:
                count += 1
            temp = temp.next

        print("Count of", num, "is:", count)

    def swap_first_last(self):
        if self.head is None or self.head.next is None:
            return

        first = self.head
        last = self.head

        while last.next:
            last = last.next

        # If there are exactly two nodes
        if first.next == last:
            last.next = first
            first.prev = last
            first.next = None
            last.prev = None
            self.head = last
            return

        # Store the surrounding nodes
        second = first.next
        second_last = last.prev

        # Update pointers
        last.prev = None
        last.next = second

        second.prev = last
        second_last.next = first

        first.prev = second_last
        first.next = None

        self.head = last

    def print(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        print("List Elements in reverse order:")

        while temp.next:
            temp = temp.next

        while temp:
            print(temp.data)
            temp = temp.prev


list1 = LinkedList()

list1.append(Node(12))
list1.append(Node(13))
list1.append(Node(14))

list1.print()

list1.occurence(12)

list1.swap_first_last()

print("After swapping first and last nodes:")
list1.print()
