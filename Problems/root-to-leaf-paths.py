class Solution:
    def printArray(self,ints):
        return list(ints)
    def printPathsUtil(self, node, path, paths):
        if not node:
            return 
        path.append(node.data)
        
        if not node.left and not node.right:
            paths.append(self.printArray(path))
        else:
            self.printPathsUtil(node.left, path, paths)
            self.printPathsUtil(node.right, path, paths)
        
        path.pop()
    def Paths(self, root):
        # code here
        paths = []
        
        self.printPathsUtil(root, [], paths)
        return paths