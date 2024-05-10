ar = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']

def left_child_ind(ind):
    return 2*ind + 1 
def right_child_ind(ind):
    return 2*ind + 2 
def data(ind):
    if 0 <= ind < len(ar): 
        return ar[ind] 
    return None 

rightChild = right_child_ind(0)
leftChild = left_child_ind(rightChild)
dataInd = data(leftChild)

print(dataInd)