class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, x):
        self.main_stack.append(x)
        # If the min_stack is empty or the new element is smaller or equal to the top of min_stack
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if not self.main_stack:
            return -1
        popped = self.main_stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
        return popped

    def getMin(self):
        if not self.min_stack:
            return -1
        return self.min_stack[-1]

# Example usage
min_stack = MinStack()
min_stack.push(2)
min_stack.push(3)
print(min_stack.pop())    # Output: 3
print(min_stack.getMin()) # Output: 2
min_stack.push(1)
print(min_stack.getMin()) # Output: 1
