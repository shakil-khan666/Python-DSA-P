#206. Reverse Linked List(leet code)

from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return 
        reversed = head
        if head.next:
            reversed = self.reverseList(head.next)
            right = head.next
            right.next = head
        head.next  = None
        return reversed
            
        
def ListTOLinked(arr):
    dummy = ListNode(-1)
    tail = dummy
    for val in arr:
        tail.next = ListNode(val)
        tail = tail.next
    return dummy.next

def dispaly(head):
    current = head
    while current:
        print(current.val,end="->")
        current = current.next
    print("None")


arr = [1,2,3,4,5]
list1=ListTOLinked(arr)
s =  Solution()
result = s.reverseList(list1)
dispaly(result)