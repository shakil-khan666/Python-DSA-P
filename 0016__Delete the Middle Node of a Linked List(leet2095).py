class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None  # একটাই node থাকলে None ফেরত

        slow = head
        fast = head
        prev = None  # middle এর previous node

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # delete middle node
        prev.next = slow.next
        return head
# helper functions
def ListTolinkList(arr):
    dummy = ListNode(-1)
    tail = dummy
    for num in arr:
        tail.next = ListNode(num)
        tail = tail.next
    return dummy.next

def display(head):
    current = head
    while current:
        print(current.val, end='->')
        current = current.next
    print('None')


arr = [1,3,4,7,1,2,6] 
list1 = ListTolinkList(arr)

s = Solution()
final = s.deleteMiddle(list1)
display(final)
