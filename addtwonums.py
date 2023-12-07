class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    # Initialize current node to dummy head of the returning list.
    dummy_head = ListNode(0)
    current = dummy_head
    carry = 0

    # Loop through lists l1 and l2 until you reach both ends.
    while l1 or l2:
        # At the start of each iteration, we should add carry from last iteration to the total sum.
        total_sum = carry
        # Set carry to 0.
        carry = 0

        # Add the values of the current nodes of l1 and l2 to total_sum.
        if l1:
            total_sum += l1.val
            l1 = l1.next
        if l2:
            total_sum += l2.val
            l2 = l2.next

        # If the total_sum is >= 10, set carry to 1 and subtract 10 from total_sum.
        if total_sum >= 10:
            carry = 1
            total_sum -= 10

        # Append total_sum to the returning list.
        current.next = ListNode(total_sum)
        # Move the current pointer to the next node.
        current = current.next

    # After the end of the loop, we add the carry to the returning list if it's not equal to 0.
    if carry > 0:
        current.next = ListNode(carry)

    # Return the next node of dummy_head, because dummy_head was used as a placeholder for the head of the returning list.
    return dummy_head.next
