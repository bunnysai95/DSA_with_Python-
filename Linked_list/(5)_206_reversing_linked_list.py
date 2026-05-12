from typing import Optional
from _0_base_helper import ListNode, build_list, print_list

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # x-> y-> z  x = prev, y = curr, z = next
        x = None        
        y = head        
        while y is not None:
            z = y.next  # the node AHEAD   (save it before we break the chain)
            y.next = x  # flip y's arrow to point backward at x
            x = y       # x walks forward to y
            y = z       # y walks forward to z
        return x        # x is the new head when y falls off the end

if __name__ == "__main__":
    head = build_list([1, 2, 3, 4, 5])
    reversed_head = Solution().reverseList(head)
    print_list(reversed_head)   # 5 -> 4 -> 3 -> 2 -> 1

"""
we are storing x y z makeing x as prev, y as curr and z as next
"""