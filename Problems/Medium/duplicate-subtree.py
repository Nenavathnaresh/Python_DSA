class Solution:

    def __init__(self):
        # Initialize a dictionary to keep track of subtree serializations

        # self.map = defaultdict(int)
        self.result = []

    def helper(self, root):
        if not root:
            return ""

        # Serialize the current subtree
        left = self.helper(root.left)
        right = self.helper(root.right)
        curr = "{} {} {}".format(root.data, left, right)

        # Check if the serialization is a duplicate
        if self.map[curr] == 1:
            self.result.append(root)

        # Update the count of the current subtree serialization
        self.map[curr] += 1

        return curr

    def printAllDups(self, root):
        self.helper(root)
        self.result.sort(key=lambda node: node.data)
        return self.result