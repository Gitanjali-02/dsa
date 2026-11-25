class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
    def insert(self,newnode):
        if self.root is None: # creating the root node
            self.root = newnode
            return
        else:
            temp = self.root
            while True:
                if newnode.data < temp.data:
                    if temp.left is None:
                        temp.left = newnode
                        return
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = newnode
                        return
                    else:
                        temp = temp.right
    def inorder(self,rt): #recursive
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data,end=" ")
            self.inorder(rt.right)
    def find_minmax(self,rt):
        temp = rt
        while temp.left:
            temp = temp.left
        print("\nMin value : ",temp.data)
        temp = rt
        while temp.right:
            temp = temp.right
        print("\nMax value : ",temp.data)
b = BST()
b.insert(Node(10))
b.insert(Node(5))
b.insert(Node(20))
b.insert(Node(-2))
b.insert(Node(7))
b.insert(Node(15))
b.insert(Node(30))
print("Display in inorder")
b.inorder(b.root)
b.find_minmax(b.root)

                