class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root):
    def check(node, low, high):
        if node is None:
            return True

        if not (low < node.val < high):
            return False

        return (check(node.left, low, node.val) and
                check(node.right, node.val, high))

    return check(root, float('-inf'), float('inf'))


# Create a binary tree
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)

# Check whether it is a valid BST
if isValidBST(root):
    print("Valid BST")
else:
    print("Invalid BST")