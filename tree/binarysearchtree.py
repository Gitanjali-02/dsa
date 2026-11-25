# Binary search tree
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
    def del_node(self,rt,val):
        if rt is None:
            return
        if val<rt.data:
            rt.left=self.del_node(rt.left,val)
        elif val>rt.data:
            rt.right=self.del_node(rt.right,val)
        else:
            if rt.left is None: #node with right child only
                return rt.right
            if rt.right is None:#node with left child only
                return rt.left
            #node has left and right chilren
            succ=self.get_successor(rt)
            rt.data=succ.data
            rt.right=self.del_node(rt.right,succ.data)
            return rt

    def get_successor(self,temp):
        temp=temp.right
        while temp.left is not None :
            temp=temp.left
        return temp



            
        

def inorder(temp): #recursive
    if temp is None:
        return
    else:
        inorder(temp.left)
        print(temp.data,end=" ")
        inorder(temp.right)
def preorder(temp): #recursive
    if temp is None:
        return
    else:
        print(temp.data,end=" ")
        inorder(temp.left)
        inorder(temp.right)
def postorder(temp): #recursive
    if temp is None:
        return
    else:
        inorder(temp.left)
        inorder(temp.right)
        print(temp.data,end=" ")
b = BST()
b.insert(Node(10))
b.insert(Node(5))
b.insert(Node(20))
b.insert(Node(-2))
b.insert(Node(7))
b.insert(Node(15))
b.insert(Node(30))
print("Display in inorder")
inorder(b.root)
print()
print("Display in preorder")
preorder(b.root)
print()
print("Display in postorder")
postorder(b.root)
b.del_node(b.root,10)
print("\nAfter deletion")
inorder(b.root)