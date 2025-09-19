from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def beforeMiddleNode(self, head: 'ListNode') -> 'ListNode':
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow 
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = None
        right = head
        while right:
            right_next = right.next
            right.next = left
            left = right
            right = right_next
        return left 

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        before_mid = self.beforeMiddleNode(head)
        sec_head = before_mid.next
        before_mid.next = None  # disconnect first half

        sec_head_rev = self.reverseList(sec_head)

        # Merge two halves
        h1, h2 = head, sec_head_rev
        while h2:
            h1_next = h1.next
            h2_next = h2.next

            h1.next = h2
            h2.next = h1_next

            h1 = h1_next
            h2 = h2_next

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
        print(current.val, end="->")
        current = current.next
    print("None")

arr = [1, 2, 3, 4, 5]
list1 = ListTOLinked(arr)
s = Solution()
s.reorderList(list1)   # modifies in place
dispaly(list1)


        