# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # basic case
        if not head:
            return False
        # rest of cases
        past_nodes = []
        while head.next:
            if head in past_nodes:
                return True
            else:
                past_nodes.append(head)
                head = head.next
        return False     
        
def create_list(arr, pos):
	# works for len(arr) > 2
	head = ListNode(arr[0])
	curr_node = head
	cycle_node = None
	for i, el in enumerate(arr[1:]):
		temp_node = ListNode(el)
		curr_node.next = temp_node
		curr_node = curr_node.next
		if i+1 == pos:
			cycle_node = curr_node

	if cycle_node:
		curr_node.next = cycle_node

	return head

head = create_list([-21,10,17,8,4,26,5,35,33,-7,-16,27,
	-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5],-1)

assert Solution().hasCycle(head) == False