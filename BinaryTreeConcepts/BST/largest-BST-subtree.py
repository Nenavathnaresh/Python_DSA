class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class Result:
    def __init__(self):
        self.max_size = 0

def largestBSTUtil(node):
    if node is None:
        return (0, True, float('inf'), float('-inf'))

    if node.left is None and node.right is None:
        return (1, True, node.data, node.data)

    l_size, l_is_bst, l_min, l_max = largestBSTUtil(node.left)
    r_size, r_is_bst, r_min, r_max = largestBSTUtil(node.right)

    if l_is_bst and r_is_bst and l_max < node.data < r_min:
        size = 1 + l_size + r_size
        return (size, True, min(l_min, node.data), max(r_max, node.data))

    return (max(l_size, r_size), False, 0, 0)

def largestBST(node):
    result = Result()
    def helper(node):
        if node is None:
            return (0, True, float('inf'), float('-inf'))
        
        if node.left is None and node.right is None:
            result.max_size = max(result.max_size, 1)
            return (1, True, node.data, node.data)

        l_size, l_is_bst, l_min, l_max = helper(node.left)
        r_size, r_is_bst, r_min, r_max = helper(node.right)

        if l_is_bst and r_is_bst and l_max < node.data < r_min:
            size = 1 + l_size + r_size
            result.max_size = max(result.max_size, size)
            return (size, True, min(l_min, node.data), max(r_max, node.data))
        
        return (max(l_size, r_size), False, 0, 0)

    helper(node)
    return result.max_size

# Example Usage
if __name__ == '__main__':
    root1 = Node(1)
    root1.left = Node(4)
    root1.right = Node(4)
    root1.left.left = Node(6)
    root1.left.right = Node(8)
    print(largestBST(root1))  # Output: 1

    root2 = Node(6)
    root2.left = Node(6)
    root2.right = Node(2)
    root2.left.right = Node(2)
    root2.right.left = Node(1)
    root2.right.right = Node(3)
    print(largestBST(root2))  # Output: 3
