class Node:
    """Node for singly linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """Solution for removing duplicates from sorted linked list."""

    def deleteDuplicates(self, head):
        """
            Head of the modified linked list with duplicates removed
        """
        current = head

        while current and current.next:
            if current.val == current.next.val:
                # Skip the duplicate node
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next

        return head


def create_linked_list(values):
    """
        Head of the created linked list, or None if empty list
    """
    if not values:
        return None

    head = Node(values[0])
    current = head

    for val in values[1:]:
        current.next = Node(val)
        current = current.next

    return head
def print_list(head):
        while head:
            print(head.val, end=' ')
            head = head.next
        print()


l=create_linked_list([1,2,3,3,3])
print_list(l)
sol=Solution()
result=(sol.deleteDuplicates(l))
print_list(result)