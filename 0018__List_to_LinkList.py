class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def List_toLinkedList(arr):
    dummy = Node(-1)
    tail  = dummy

    for val in arr:
        tail.next = Node(val)
        tail = tail.next
    return dummy.next

arr = [1, 2, 3, 4, 5]
linked_list = List_toLinkedList(arr)

def display(head):
    current = head 
    while current:
        print(current.data ,end='->')
        current =  current.next
    print('None')

display(linked_list)