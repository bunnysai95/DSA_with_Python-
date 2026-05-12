import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from _0_base_helper import ListNode, build_intersecting_lists
from typing import Optional

class Solution:
    def getIntersectionNode(self, headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
        l1 = headA
        l2 = headB
        while l1 != l2:
            if l1:
                l1 = l1.next
            else:
                l1 = headB
            if l2:
                l2 = l2.next
            else:
               l2 = headA
        return l1


listA_vals = [4, 1]        # unique prefix of A (skipA = 2)
listB_vals = [5, 6, 1]    # unique prefix of B (skipB = 3)
common     = [8, 4, 5]    # shared tail starting at intersection

headA, headB = build_intersecting_lists(listA_vals, listB_vals, common)

result = Solution().getIntersectionNode(headA, headB)
print("Intersected at node with value:", result.val if result else None)

"""
we are checking l1 and l2 are not null 
when l1 and l2 are null returning null
when l1 is null continuing to l2 head 
when l2 is null continue to l1 head 
when both l1 and l2 are same returning l1 (or) l2 == both are same values
"""