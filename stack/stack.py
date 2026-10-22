class Node:
    def __init__(self , value):
        self.data=value
        self.next=None
class stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None
    def push(self,new_node):
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            temp=self.top
            print("\npoped element:",temp.data)
            self.top=self.top.next
            temp=None

    def print(self):
        if self.isempty():
            print("stack is empty")
        else:

            print("stack contains:")
            temp=self.top
            while temp:
                print(temp.data,end=" ")
                temp=temp.next
obj=stack()
obj.push(Node(1))
obj.push(Node(2))
obj.push(Node(3))
obj.push(Node(4))
obj.print()
obj.pop()
obj.print()
