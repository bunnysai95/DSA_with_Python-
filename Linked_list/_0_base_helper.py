from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(values: List[int]) -> Optional[ListNode]:
    """Convert [1,2,3] -> 1 -> 2 -> 3"""
    dummy = ListNode()
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def print_list(head: Optional[ListNode]) -> None:
    """Print 1 -> 2 -> 3 -> None"""
    vals = []
    while head:
        vals.append(str(head.val))
        head = head.next
    print(" -> ".join(vals) if vals else "None")

def build_intersecting_lists(listA: List[int], listB: List[int], common: List[int]):
    """Build two lists that share a common tail. Returns (headA, headB)."""
    shared = build_list(common)
    headA = build_list(listA)
    headB = build_list(listB)
    # attach shared tail to both
    if headA:
        tail = headA
        while tail.next: tail = tail.next
        tail.next = shared
    else:
        headA = shared
    if headB:
        tail = headB
        while tail.next: tail = tail.next
        tail.next = shared
    else:
        headB = shared
    return headA, headB