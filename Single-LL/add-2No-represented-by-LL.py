class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    #Function to add two numbers represented by linked list.
    def reverse(self, head):
        prev = None
        curr = head 
        next = None 
        
        while curr:
            next = curr.next 
            curr.next = prev 
            prev = curr 
            curr = next 
        return prev 
    def addTwoLists(self, num1, num2):
        # code here
        # return head of sum list
        num1 = self.reverse(num1)
        num2 = self.reverse(num2)
        
        sumList = None 
        carry = 0 
        
        while num1 or num2 or carry>0:
            newVal = carry 
            
            if num1:
                newVal += num1.data 
            if num2:
                newVal += num2.data 
                
            carry = newVal // 10 
            newVal = newVal%10 
            
            newNode = Node(newVal)
            newNode.next = sumList 
            sumList = newNode 
            
            if num1:
                num1 = num1.next 
            if num2 :
                num2 = num2.next 
        while sumList and sumList.data == 0:
            temp = sumList.next 
            sumList.next = None 
            sumList = temp 
        if sumList is None:
            return Node(0)
        return sumList 