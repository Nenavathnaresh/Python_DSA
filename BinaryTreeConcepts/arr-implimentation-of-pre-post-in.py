ar = ['R', 'A', 'B', 'C', 'D', 'E', 'F', None, None, None, None, None, None, 'G']

def left_child_ind(ind):
    return 2*ind + 1 
def right_child_ind(ind):
    return 2*ind + 2 

def preOrder(ind):
    if ind >= len(ar) or ar[ind] is None:
        return []
    return [ar[ind]] + preOrder(left_child_ind(ind)) + preOrder(right_child_ind(ind)) 

def inOrder(ind):
    if ind >= len(ar) or ar[ind] is None:
        return []
    return inOrder(left_child_ind(ind)) + [ar[ind]] + inOrder(right_child_ind(ind)) 

def postOrder(ind):
    if ind >= len(ar) or ar[ind] is None:
        return []
    return postOrder(left_child_ind(ind)) + postOrder(right_child_ind(ind)) + [ar[ind]]

print("preOrder :", preOrder(0))
print("inOrder :", inOrder(0))
print("postOrder :", postOrder(0))
    
