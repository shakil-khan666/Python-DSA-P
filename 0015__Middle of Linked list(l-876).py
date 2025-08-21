
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      
        self.next = next    

class Solution:
    def middleNode(self, head: 'ListNode') -> 'ListNode':
        slow = head
        fast = head

        
        while fast and fast.next:
            slow = slow.next       
            fast = fast.next.next   

        
        return slow



node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)


sol = Solution()
middle = sol.middleNode(node1)


while middle:
    print(middle.val, end=" → ")
    middle = middle.next
