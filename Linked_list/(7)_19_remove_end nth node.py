# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from _0_base_helper import ListNode, build_list, print_list
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # slow = head 
        # fast = head
        # for _ in range(n):
        #     fast = fast.next
        # if not fast:
        #     return head.next 
        # while fast.next: 
        #     fast = fast.next
        #     slow = slow.next 
        # slow.next = slow.next.next
        # return head 
        dummy = ListNode(0, head)
        left = dummy 
        right = head 
        while right != None and n > 0 :
            right = right.next 
            n -= 1
        while right != None:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next

if __name__ == "__main__":
    # [1,2,3,4,5], n=2 → remove 4th node → [1,2,3,5]
    head = build_list([1, 2, 3, 4, 5])
    result = Solution().removeNthFromEnd(head, 2)
    print_list(result)   # 1 -> 2 -> 3 -> 5

    # [1,2], n=1 → remove last → [1]
    head = build_list([1, 2])
    result = Solution().removeNthFromEnd(head, 1)
    print_list(result)   # 1

    # [1], n=1 → remove only node → None
    head = build_list([1])
    result = Solution().removeNthFromEnd(head, 1)
    print_list(result)   # None
