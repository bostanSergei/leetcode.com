from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    count = 0
    curr_node = head
    while curr_node:
        curr_node = curr_node.next
        count += 1

    curr_node = head
    for i in range(count // 2):
        curr_node = curr_node.next

    return curr_node
