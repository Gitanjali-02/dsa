class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            val = int(input("Enter node value: "))
            self.append(Node(val))
    
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")
    
    def insert(self, new_node, pos):
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        p = 1

        while temp is not None and p < pos - 1:
            temp = temp.next
            p += 1

        if temp is None:
            print("Invalid position")
            return

        new_node.next = temp.next
        temp.next = new_node

    def middle(self):
        if self.head is None:
            print("Linked List is empty")
            return
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        print("Middle node value:", slow.data)
    
    def delete(self, val):
        if self.head is None:
            print("Linked List is empty")
            return
        if self.head.data == val:
            self.head = self.head.next
            print("Node deleted")
            return
        temp = self.head
        while temp.next is not None:
            if temp.next.data == val:
                temp.next = temp.next.next
                print("Node deleted")
                return
            temp = temp.next
        print("Value not found")
 
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        print("Linked List reversed")

    def consecutive_sum(self):
        if self.head is None or self.head.next is None:
            print("At least two nodes are required")
            return
        temp = self.head
        while temp.next is not None:
            total = temp.data + temp.next.data
            print(temp.data, "+", temp.next.data, "=", total)
            temp = temp.next

ll = LinkedList()
while True: 
    print("1. Create Linked List")
    print("2. Traverse and Print")
    print("3. Insert at Specific Position")
    print("4. Find Middle Node")
    print("5. Delete Node")
    print("6. Reverse Linked List")
    print("7. Sum of Consecutive Nodes")
    print("8. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        ll.create()
    elif choice == 2:
        ll.print()
    elif choice == 3:
        val = int(input("Enter value to insert: "))
        pos = int(input("Enter position: "))
        ll.insert(Node(val), pos)

    elif choice == 4:
        ll.middle()

    elif choice == 5:
        val = int(input("Enter value to delete: "))
        ll.delete(val)

    elif choice == 6:
        ll.reverse()

    elif choice == 7:
        ll.consecutive_sum()

    elif choice == 8:
        print("Program ended")
        break

    else:
        print("Invalid choice")
