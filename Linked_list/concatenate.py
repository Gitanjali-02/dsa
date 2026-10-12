
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Append a node
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # Find and delete the middle node
    def findmid_del(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            print("Middle node:", self.head.data)
            self.head = None
            return

        temp = temp1 = self.head
        prev = None

        while temp1 and temp1.next:
            prev = temp
            temp = temp.next
            temp1 = temp1.next.next

        print("Middle node:", temp.data)
        prev.next = temp.next

    # Delete the first and last nodes
    def delfirst_last(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        self.head = self.head.next

        temp = self.head
        prev = None

        while temp.next:
            prev = temp
            temp = temp.next

        prev.next = None

    # Delete alternate nodes
    def del_alternate(self):
        prev = self.head

        while prev and prev.next:
            temp = prev.next
            prev.next = temp.next
            prev = prev.next

    # Concatenate two linked lists
    def concatenate(self, list2):
        if self.head is None:
            self.head = list2.head
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = list2.head

    # Print the linked list
    def print(self):
        print("List elements:")
        temp = self.head

        while temp:
            print(temp.data, end=" ")
            temp = temp.next

        print()


list1 = LinkedList()
list2 = LinkedList()

for value in [10, 20, 30, 40, 55]:
    list1.append(Node(value))

for value in [2, 3, 4]:
    list2.append(Node(value))

list1.print()
list2.print()

list1.concatenate(list2)
list1.print()
