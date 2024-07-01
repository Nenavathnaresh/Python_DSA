class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_inorder_postorder(inorder, postorder):
    if not inorder or not postorder:
        return None

    # The last element in postorder is the root
    root_val = postorder.pop()
    root = TreeNode(root_val)
    
    # Find the index of the root in inorder
    inorder_index = inorder.index(root_val)
    
    # Build the right subtree before the left subtree
    # since we are consuming postorder from the end
    root.right = build_tree_from_inorder_postorder(inorder[inorder_index+1:], postorder)
    root.left = build_tree_from_inorder_postorder(inorder[:inorder_index], postorder)
    
    return root

def preorder_traversal(root):
    if root is None:
        return []
    return [root.val] + preorder_traversal(root.left) + preorder_traversal(root.right)

# Example usage:
n = 8
inorder = [4, 8, 2, 5, 1, 6, 3, 7]
postorder = [8, 4, 5, 2, 6, 7, 3, 1]

root = build_tree_from_inorder_postorder(inorder, postorder)
print(preorder_traversal(root))
