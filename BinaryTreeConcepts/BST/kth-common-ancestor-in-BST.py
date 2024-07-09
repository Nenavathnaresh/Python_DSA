class TreeNode:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def kthCommonAncestor(root, k, x, y):
    def findLCA(node, x, y):
        if not node:
            return None
        if node.data > x and node.data > y:
            return findLCA(node.left, x, y)
        if node.data < x and node.data < y:
            return findLCA(node.right, x, y)
        return node

    def findKthAncestorFromNode(node, k):
        stack = []
        while node and k > 0:
            stack.append(node)
            node = node.parent
            k -= 1
        return stack[-1].data if k == 0 else -1

    # Augment the tree nodes to keep track of parent pointers
    def augmentWithParents(node, parent=None):
        if node:
            node.parent = parent
            augmentWithParents(node.left, node)
            augmentWithParents(node.right, node)
    
    augmentWithParents(root)
    
    lca = findLCA(root, x, y)
    
    if not lca:
        return -1
    
    return findKthAncestorFromNode(lca, k)

# Helper function to insert a new node with given key in BST
def insert(node, key):
    if node is None:
        return TreeNode(key)
    if key < node.data:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

# Example usage:
# Constructing the tree
root = TreeNode(50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

k = 2
x = 40
y = 60

print(kthCommonAncestor(root, k, x, y))  # Output: -1
