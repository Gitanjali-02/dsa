
class Stack:
    def __init__(self):
        self.stack = []

    # Insert element
    def push(self, element):
        self.stack.append(element)
        print(element, "pushed into stack")

    # Delete top element
    def pop(self):
        if not self.stack:
            print("Stack is empty")
        else:
            print("Popped element:", self.stack.pop())

    # Display stack
    def display(self):
        if not self.stack:
            print("Stack is empty")
        else:
            print("Stack elements (Top to Bottom):")
            for i in reversed(self.stack):
                print(i)

    # Reverse string using stack
    def reverse_string(self, string):
        temp = []

        for ch in string:
            temp.append(ch)

        result = ""
        while temp:
            result += temp.pop()

        print("Reversed string:", result)

    # Reverse stack using another stack
    def reverse_stack(self):
        temp = []

        while self.stack:
            temp.append(self.stack.pop())

        self.stack = temp
        print("Stack reversed successfully")


s = Stack()

while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Reverse String")
    print("5. Reverse Stack")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = int(input("Enter element: "))
        s.push(element)

    elif choice == 2:
        s.pop()

    elif choice == 3:
        s.display()

    elif choice == 4:
        string = input("Enter a string: ")
        s.reverse_string(string)

    elif choice == 5:
        s.reverse_stack()

    elif choice == 6:
        print("Program terminated")
        break

    else:
        print("Invalid choice")
