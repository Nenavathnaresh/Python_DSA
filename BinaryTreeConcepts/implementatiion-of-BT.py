class TreeNode:
    def __init__(self,data):
        self.data = data 
        self.left = None 
        self.right = None
root = TreeNode('R')
nodeA = TreeNode("A")
nodeB = TreeNode("B")
nodeC = TreeNode("c")
nodeD = TreeNode("D")
nodeE = TreeNode("E")
nodeF = TreeNode("F")
nodeG = TreeNode("G")

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF 

nodeC.left = nodeG

print(root.left.right.data)
        