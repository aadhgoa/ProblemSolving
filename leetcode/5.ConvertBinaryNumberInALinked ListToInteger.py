"""
1290. Convert Binary Number in a Linked List to Integer

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

Example 1:
Input: head = [1,0,1]
Output: 5
Explanation: (1 * 2^2 + 0 * 2^1 + 1 * 2^0 = 5)

Intution:
1. Initialize a variable `result` to 0.
2. Traverse the linked list:
   - For each node, shift `result` to the left by 1 (equivalent to multiplying by 2).
   - Add the current node's value to `result`.
3. Return `result` after traversing the entire list.
"""


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None): # type: ignore
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        result = 0
        current = head

        while current:
            # Shift result to the left 
            result  = (result << 1) | current.val

            # Move to the next node
            current = current.next
        return result
    
    
def main():
    # Example usage:
    # Creating a linked list representing the binary number 101 (which is 5 in decimal)
    head = ListNode(1, ListNode(0, ListNode(1)))
    
    solution = Solution()
    print(solution.getDecimalValue(head))  # Output: 5

if __name__ == "__main__":
    main()