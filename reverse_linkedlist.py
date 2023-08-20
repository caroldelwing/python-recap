class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def reverseList(head: ListNode) -> ListNode:
    curr = head
    pre = None
    nxt = None
    while curr:
        nxt = curr.next  # hold the next address of curr
        curr.next = pre  # connect current to pre " <- " (reverse node)
        pre = curr  # move previous
        curr = nxt  # move curr

    return pre

node4 = ListNode(4)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

reversed_head = reverseList(node1)

# Printing the reversed linked list: 4 -> 3 -> 2 -> 1
current = reversed_head
while current:
    print(current.val, end=" -> ")
    current = current.next
