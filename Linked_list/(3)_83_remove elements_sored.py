from typing import Optional
head = [1,1,2,3,3]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

def build_list(arr): # helper function to build a linked list from an array
    dummy = ListNode() # creating a dummy node to simplify edge cases
    curr = dummy
    for x in arr:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next
def print_list(head): # helper function to print a linked list as an array
    res = [] # defining an empty list
    while head:
        res.append(head.val)
        head = head.next
    print(res)
solution = Solution() #calling class solution 
list1 = build_list([1,1,2,3,3]) # defining list1
result = solution.deleteDuplicates(list1)
print_list(result)
