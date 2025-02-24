from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)  # Dummy node to track the result
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # Get value from l1 (or 0 if l1 is None)
            val2 = l2.val if l2 else 0  # Get value from l2 (or 0 if l2 is None)

            # Compute sum and carry
            total = val1 + val2 + carry
            carry = total // 10  # Carry for the next digit
            current.next = ListNode(total % 10)  # Store single digit in new node
            
            # Move to next node
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy_head.next  # Return the next node (skip dummy head) 

# Helper function to create a linked list from a list
def create_linked_list(lst):
    dummy_head = ListNode()
    current = dummy_head
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy_head.next

# Helper function to print a linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))

if __name__ == "__main__":
    solution = Solution()

    # Test case 1: [2,4,3] + [5,6,4] = [7,0,8]
    l1 = create_linked_list([2,4,3])
    l2 = create_linked_list([5,6,4])
    result = solution.addTwoNumbers(l1, l2)
    print("Output 1:")
    print_linked_list(result)  # Expected: 7 -> 0 -> 8

    # Test case 2: [0] + [0] = [0]
    l1 = create_linked_list([0])
    l2 = create_linked_list([0])
    result = solution.addTwoNumbers(l1, l2)
    print("Output 2:")
    print_linked_list(result)  # Expected: 0

    # Test case 3: [9,9,9,9,9,9,9] + [9,9,9,9] = [8,9,9,9,0,0,0,1]
    l1 = create_linked_list([9,9,9,9,9,9,9])
    l2 = create_linked_list([9,9,9,9])
    result = solution.addTwoNumbers(l1, l2)
    print("Output 3:")
    print_linked_list(result)  # Expected: 8 -> 9 -> 9 -> 9 -> 0 -> 0 -> 0 -> 1
