class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self,newnode):
        if self.root is None:
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
    def inorder(self,root):
        if root is None:
            return
        else:
            self.inorder(root.left)
            print(root.data ,end=" ")
            self.inorder(root.right)
    def level_order(self,root):
        if root is None:
            print("BST is empty")
            return
        arr = []
        cnt = 0
        level = 0
        arr.append(root)
        while cnt < len(arr):
            node_count = len(arr) - cnt # no of node to be visited
            print("\nLevel ",level,": ",end =" ")
            for i in range(node_count):
                temp = arr[cnt]
                cnt += 1
                print(temp.data,end =" ")
                if temp.left:
                    arr.append(temp.left)
                if temp.right:
                    arr.append(temp.right)
            level += 1
        print("\nHeight of tree : ",level-1)
b = BST()
b.insert(Node(100))
b.insert(Node(10))
b.insert(Node(450))
b.insert(Node(4))
b.insert(Node(65))
b.insert(Node(300))
b.insert(Node(500))
b.insert(Node(50))
b.insert(Node(70))
b.inorder(b.root)
print("\nLevel order")
b.level_order(b.root)
        