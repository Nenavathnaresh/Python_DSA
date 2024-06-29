def deleteMid(stack, sizeOfStack):
    # Helper function to delete the middle element
    def deleteMidUtil(stack, currentIndex, middleIndex):
        # Base case: If stack is empty or we have reached the middle index
        if currentIndex == middleIndex:
            stack.pop()
            return
        
        # Pop the top element
        topElement = stack.pop()
        
        # Recursive call to reach the middle element
        deleteMidUtil(stack, currentIndex + 1, middleIndex)
        
        # Push the elements back except the middle one
        stack.append(topElement)
    
    # Calculate the middle index
    middleIndex = sizeOfStack // 2
    
    # Call the utility function
    deleteMidUtil(stack, 0, middleIndex)

# Example usage:
stack1 = [10, 20, 30, 40, 50]
deleteMid(stack1, len(stack1))
print(stack1)  # Output: [10, 20, 40, 50]

stack2 = [10, 20, 30, 40]
deleteMid(stack2, len(stack2))
print(stack2)  # Output: [10, 30, 40]


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def deleteMid(self, s, sizeOfStack):
        # code here
        if sizeOfStack % 2 == 0:
            s.pop((sizeOfStack-1)//2)
        else:
            s.pop((sizeOfStack)//2)
        return s