from typing import Optional
from _0_base_helper import ListNode, build_list, print_list

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head 
        while fast and fast.next:
            assert slow is not None
            slow = slow.next
            fast = fast.next.next
        return slow
    
if __name__ == "__main__":
    head = build_list([1, 2, 3, 4, 5])
    middle_node = Solution().middleNode(head)
    assert middle_node is not None
    print(middle_node.val)   # 3