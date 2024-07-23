class Solution:
    def merge(self, root1, root2):
        # code here
        res = []
        def traversal(node):
            if node:
                traversal(node.left)
                res.append(node.data)
                traversal(node.right)
        traversal(root1)
        traversal(root2)
        res.sort()
        return res