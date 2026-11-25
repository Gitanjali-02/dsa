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
    def inorder(self,rt): #recursive
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data,end=" ")
            self.inorder(rt.right)
    def del_node(self,root,val):
        if root is None:
            return root
        if val < root.data:
            root.left = self.del_node(root.left, val)
        elif val > root.data:
            root.right = self.del_node(root.right, val)
        else:
            if root.left is None:  # node with right child only
                return root.right
            if root.right is None:
                return root.left  # node with left child only
            # node has both left and right children
            succ = self.get_successor(root)
            root.data = succ.data
            root.right = self.del_node(root.right,succ.data)
        return root
    def get_successor(self,temp):
        temp = temp.right
        while temp.left is not None:
            temp = temp.left
        return temp

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
print()
print("After Deletion : ")
b.del_node(b.root,10)
b.inorder(b.root)


                