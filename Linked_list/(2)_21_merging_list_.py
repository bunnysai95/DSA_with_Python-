from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_list = ListNode()
        tail = dummy_list

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next   # keep this outside

        if list1:
            tail.next = list1
        else:
            tail.next = list2 

        return dummy_list.next

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
list1 = build_list([1,2,4]) # defining list1
list2 = build_list([1,3,4]) # defining list2
result = solution.mergeTwoLists(list1, list2)
print_list(result)