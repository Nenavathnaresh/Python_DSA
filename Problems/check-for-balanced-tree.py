def isBalancedUtil(self, root):
    if not root:
        return True,0
    left_balanced, left_height = self.isBalancedUtil(root.left)
    if not left_balanced:
        return False,0
    
    right_balanced, right_height = self.isBalancedUtil(root.right)
    if not right_balanced :
        return False,0
    
    if abs(left_height - right_height) > 1:
        return False,0
    return True, 1 + max(left_height, right_height)
def isBalanced(self, root):
    balanced, _ = self.isBalancedUtil(root)
    return balanced