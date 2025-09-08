class ListNode:
    def __init__(self, data):
        self.data =  data 
        self.next = None

class Solution:
    def middleNode(self, head):
        if not head or not head.next:
            return head
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def DeletNode(self, head):
        if not head or not head.next:
            return None
        
        mid = self.middleNode(head)
        
        
        if mid.next:
            mid.data = mid.next.data
            mid.next = mid.next.next
        else:
            return None  

        return head

def ListTolinkList(arr):
    dummy = ListNode(-1)
    tail = dummy
    for num in arr:
        tail.next = ListNode(num)
        tail = tail.next
    return dummy.next 

def display(head):
    current =  head
    while current:
        print(current.data,end='->')
        current = current.next
    print('None')


arr = [1,3,4,7,1,2,6] 
list1 = ListTolinkList(arr)

s = Solution()
final = s.DeletNode(list1)   
display(final)
