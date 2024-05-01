class node:
    def __init__(self, val):
        self.data = val
        self.next = None



class Solution:
    #Function to reverse a linked list.
    def isVowel(self,char):
        return char in ['a', 'e', 'i', 'o', 'u']
        
    def arrangeCV(self, head):
        # Code here
        newHead = head
        latestVowel = None 
        curr = head 
        
        if head is None:
            return None 
        
        if self.isVowel(head.data):
            latestVowel = head 
        else:
            while curr.next is not None and not self.isVowel(curr.next.data):
                curr = curr.next 
            if curr.next is None :
                return head 
            
            latestVowel = newHead = curr.next 
            curr.next = curr.next.next
            latestVowel.next = head 
        while curr is not None and curr.next is not None:
            if self.isVowel(curr.next.data):
                if curr == latestVowel:
                    latestVowel = curr = curr.next
                else:
                    temp = latestVowel.next 
                    latestVowel.next = curr.next 
                    latestVowel = latestVowel.next 
                    curr.next = curr.next.next 
                    latestVowel.next = temp
            else:
                curr = curr.next 
        return newHead