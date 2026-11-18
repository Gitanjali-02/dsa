
class node:
    def __init__(self, value, pr):
        self.data = value
        self.priority = pr
        self.next = None


class priorityQueue:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, new_node):
        if self.front == None:
            self.front = new_node
            return

        # Insert at first position
        if self.front.priority > new_node.priority:
            new_node.next = self.front
            self.front = new_node
            return

        prev = self.front
        temp = self.front

        while temp:
            if new_node.priority < temp.priority:
                break
            else:
                prev = temp
                temp = temp.next

        prev.next = new_node
        new_node.next = temp

    def display_all(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def dequeue(self):
        if self.front == None:
            print("Priority Queue is empty")
            return

        temp = self.front
        print("Deleted node:", temp.data)

        self.front = self.front.next
        temp.next = None

    def display_next(self):
        if self.front == None:
            print("No patients waiting")
            return

        print("Next patient:", self.front.data)
        print("Priority:", self.front.priority)


pq = priorityQueue()

# Add patients
pq.enqueue(node(101, 3))
pq.enqueue(node(102, 2))
pq.enqueue(node(103, 1))
pq.enqueue(node(104, 3))
pq.enqueue(node(105, 2))

# Display all patients
print("All waiting patients:")
pq.display_all()

# Display next patient
pq.display_next()

# Remove treated patient
pq.dequeue()

# Display remaining patients
print("Remaining patients:")
pq.display_all()
