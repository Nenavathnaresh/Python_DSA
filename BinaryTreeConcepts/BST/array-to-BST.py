class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        # Helper function to build the BST
        def buildTree(start, end):
            if start > end:
                return None
            
            # Find the middle index
            mid = (start + end) // 2
            
            # Create a node with the middle element
            node = TreeNode(nums[mid])
            
            # Recursively build the left and right subtrees
            node.left = buildTree(start, mid - 1)
            node.right = buildTree(mid + 1, end)
            
            return node
        
        # Build the tree starting from the whole array
        return buildTree(0, len(nums) - 1)

# Example Usage
sol = Solution()
nums1 = [1, 2, 3, 4]
root1 = sol.sortedArrayToBST(nums1)

nums2 = [1, 2, 3, 4, 5, 6, 7]
root2 = sol.sortedArrayToBST(nums2)

# Function to check if the tree is height-balanced
def isBalanced(root):
    def check(node):
        if not node:
            return 0, True
        
        left_height, left_balanced = check(node.left)
        right_height, right_balanced = check(node.right)
        
        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1
        return max(left_height, right_height) + 1, balanced
    
    _, result = check(root)
    return result

# Check if the resulting trees are balanced
print(isBalanced(root1))  # Output: True
print(isBalanced(root2))  # Output: True
