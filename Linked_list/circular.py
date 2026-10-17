class Node:
    def __init__(self, val):
        self.data=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head= None
    def append(self, new_node):
        if (self.head==None):
            self.head=new_node
            new_node.next=self.head #to point back last node to the 1st node
        else:
            temp=self.head
            while (temp.next!=self.head):# temp.next as well
                temp = temp.next
            temp.next=new_node #appending new node
            new_node.next=self.head
            
    def del_node(self, value):
            temp=self.head
            prev = None
            if(temp.data==value):
                while (temp.next!=self.head):#find last node
                    temp=temp.next
                self.head = self.head.next
                temp.next=self.head #new line to find last node
                # return
            # while(temp):
            #     if temp.data==value:
            #         break
            else:
                while(temp.data!=value and temp):
                    
                    prev=temp
                    temp=temp.next
                    if temp==None:
                        print("Value is not there on list")
                        return
            prev.next=temp.next
            temp=None
    def print (self):
        temp=self.head
        while True:      #do while we can also use
            print(temp.data)
            temp=temp.next
            if temp==self.head:
                break
        print(temp.data) #required for circular 
list=LinkedList()
n1=Node(10)
n2=Node(20)
n3=Node(30)
list.append(n1)        
list.append(n2)        
list.append(n3)        
list.append(Node(40)) 
list.del_node(20)

list.print()       
       
        