class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        cur_node = head

        while cur_node:
            while stack and stack[-1].val < cur_node.val:
                stack.pop()

            stack.append(cur_node)

            cur_node = cur_node.next

        head = stack[0]
        cur_node = head
        for node in stack[1:]:
            cur_node.next = node
            cur_node = cur_node.next

        return head


list = "345321"

head = Node(3)
cur_node = head
for i in range(1, len(list)):
    new_node = Node(list[i])
    cur_node.next = new_node
    cur_node = cur_node.next

head = remove_nodes(head)

cur_node = head

while cur_node:
    print(cur_node.value)
    cur_node = cur_node.next
