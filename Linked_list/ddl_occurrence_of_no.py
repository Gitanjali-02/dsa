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
            
   
    def occurence(self,num):
        temp=self.head
        count=0
        
        while temp:
            if(temp.data== num):
                count+=1
            temp=temp.next
        print("count of ",num ,"is:",count)


    def print(self):
        temp = self.head
        print("List Elements:")

        while temp.next:
            #print(temp.data)
            temp = temp.next
        while(temp):
            print(temp.data,)
            temp=temp.prev

list1 = LinkedList()

list1.append(Node(12))
list1.append(Node(13))
list1.append(Node(12))
list1.print()

list1.occurence(12)
