class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def isSumTree(root):
    def check_and_sum(node):
        if node is None:
            return True, 0
        if node.left is None and node.right is None:
            return True, node.data
        
        left_is_sum_tree, left_sum = check_and_sum(node.left)
        right_is_sum_tree, right_sum = check_and_sum(node.right)
        
        current_sum = left_sum + right_sum
        
        is_current_node_sum_tree = (left_is_sum_tree and
                                    right_is_sum_tree and
                                    node.data == current_sum)
        
        return is_current_node_sum_tree, current_sum + node.data
    
    is_sum_tree, _ = check_and_sum(root)
    return is_sum_tree

# Helper function to build tree from level-order input
def build_tree(nodes):
    if not nodes or nodes[0] == 'N':
        return None

    root = Node(int(nodes[0]))
    queue = [root]
    index = 1

    while queue and index < len(nodes):
        current = queue.pop(0)

        if index < len(nodes) and nodes[index] != 'N':
            current.left = Node(int(nodes[index]))
            queue.append(current.left)
        index += 1

        if index < len(nodes) and nodes[index] != 'N':
            current.right = Node(int(nodes[index]))
            queue.append(current.right)
        index += 1

    return root

# Example usage with provided test case
nodes = ["62", "16", "15", "N", "8", "4", "7", "N", "8", "4"]
root = build_tree(nodes)

print(isSumTree(root))  # Expected Output: 1
