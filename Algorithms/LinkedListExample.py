'''

Question:

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    carry = 0
    dummy_head = ListNode(0)
    current = dummy_head
    p = l1
    q = l2

    while p or q:
        x = p.val if p else 0
        y = q.val if q else 0
        _sum = carry + x + y

        carry = _sum // 10
        current.next = ListNode(_sum % 10)
        current = current.next

        if p:
            p = p.next

        if q:
            q = q.next

        if carry > 0:
            current.next = ListNode(carry)
        return dummy_head.next


'''

Tests
l1 = [2,4,3]
l2 = [5,6,4]

'''

test_l1 = ListNode(2, ListNode(4, ListNode(3)))
test_l2 = ListNode(5, ListNode(6, ListNode(4)))

result_list = addTwoNumbers(test_l1, test_l2)


def linkedListToList(node):
    r_list = []
    while node:
        r_list.append(node.val)
        node = node.next
    return r_list


output = linkedListToList(result_list)
print(f"Output ==>> {output}")
