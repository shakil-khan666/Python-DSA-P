
from typing import Optional


class ListNode:
    def __init__(self, data):
        self.data =  data 
        self.next = None

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow =  head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast =  fast.next.next

        return slow

def ListTolinkList(arr):

    dummy = ListNode(-1)
    tail = dummy
    for num in arr:
        tail.next = ListNode(num)
        tail = tail.next
    return dummy.next 




arr = [1,2,3,4,5,6] 
list = ListTolinkList(arr)   

def display(head):
    current =  head
    while current:
        print(current.data,end='->')
        current = current.next
    print('None')

s= Solution()
final= s.middleNode(list)
display(final)