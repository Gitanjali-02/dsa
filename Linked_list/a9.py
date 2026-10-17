class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
    #creating a list
class LinkedList:
    def __init__(self):
        self.head = None
        
    #append elements or nodes into the list 
    def append(self, new_node):
        if(self.head == None):
            self.head=new_node
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node  #appending new node
            
    #display the list 
    def display(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
            
    #insert node or element at specific location
    def insertAtPos(self, new_node, pos):
            if pos == 1:
                new_node.next = self.head
                self.head = new_node
            else:
                temp = self.head
                p = 1
                while p < pos - 1 and temp is not None:
                    temp = temp.next
                    p += 1
                
                if temp is not None:
                    new_node.next = temp.next
                    temp.next = new_node
                    
    #accessing the middle element or node
    def mid_node(self):
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        mid = count//2
        temp = self.head
        n=0
        while temp and n < mid:
            temp = temp.next
            n += 1
        print(temp.data)
        
    #delete the node 
    def del_node(self, value):
        temp = self.head
        prev = None
        if(temp.data == value):
            self.head = self.head.next
            return
        while(temp):
            if(temp.data == value):
                break
            else:
                prev = temp
                temp =temp.next
        if temp == None:
            print("Value is not there in the list")
            return 
        prev.next = temp.next
    
    #reverse the list
    def reverse(self):
        temp =self.head 
        prev = None
        while temp: 
            nextnode = temp.next
            temp.next = prev
            prev = temp 
            temp = nextnode
        self.head = prev  
        
    #sum of two consecutive nodes
    def sum_of_two_nodes(self):
        temp = self.head
        sum=0
        while (temp and temp.next):
            sum = temp.data + temp.next.data
            temp = temp.next
            print(sum)

list = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
list.append(n1)
list.append(n2)
list.append(n3)
list.append(Node(40))
list.display()
list.insertAtPos(Node(100), 1)
print("Display the list")  
list.display()
print("Display middle node")
list.mid_node()
list.del_node(40)
print("Display updated list")
list.display()
list.reverse()
print("Display reverse list")
list.display()
print("Sum of two consecutive nodes")
list.sum_of_two_nodes()