def deleteNode(curr_node):
    if curr_node is None or curr_node.next is None :
        return 
    nextNOde = curr_node.next 
    curr_node.data = nextNOde.data 
    curr_node.next = nextNOde.next  
