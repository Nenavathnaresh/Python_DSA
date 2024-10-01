class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def inOrderTraversal(root, result):
    # Helper function to perform in-order traversal
    if root is None:
        return
    inOrderTraversal(root.left, result)
    result.append(root.val)
    inOrderTraversal(root.right, result)

def mergeSortedArrays(arr1, arr2):
    # Helper function to merge two sorted arrays
    i, j = 0, 0
    merged = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    
    # If there are remaining elements in arr1
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    
    # If there are remaining elements in arr2
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1
    
    return merged

def mergeBSTs(root1, root2):
    # Step 1: Perform in-order traversal on both BSTs to get sorted arrays
    list1, list2 = [], []
    
    inOrderTraversal(root1, list1)
    inOrderTraversal(root2, list2)
    
    # Step 2: Merge the two sorted arrays
    mergedList = mergeSortedArrays(list1, list2)
    
    return mergedList
