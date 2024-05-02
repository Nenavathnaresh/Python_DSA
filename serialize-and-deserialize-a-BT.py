class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    #Function to serialize a tree and return a list containing nodes of tree.
    def serialize(self, root):
        #code here
        if root is None:
            return []
    
        serialized_tree = []
        self.serializeUtil(root, serialized_tree)
        return serialized_tree
        
    def serializeUtil(self,root, a):
        if root is None:
            a.append(-1)
            return
    
        a.append(root.data)
        self.serializeUtil(root.left, a)
        self.serializeUtil(root.right, a)
    
    #Function to deserialize a list and construct the tree.   
    def deSerialize(self, a):
        #code here
        if not a:
            return None
    
        index = [0] # To keep track of the current index during deserialization
        return self.deserialize_helper(a, index)
    
    def deserialize_helper(self, a, index):
        if index[0] == len(a) or a[index[0]] == -1:
            index[0] += 1
            return None
    
        root = Node(a[index[0]])
        index[0] += 1
        root.left = self.deserialize_helper(a, index)
        root.right = self.deserialize_helper(a, index)
    
        return root