class Solution:
    def get_list_size(self, head: ListNode):
        n = 0
        while head:
            n += 1
            head = head.next
        return n
    
    def get_kmin_kmax_vals(self, head: ListNode, k_min: int, k_max: int):
        for _ in range(k_min):
            head = head.next
        k_min_val = head.val
        for _ in range(k_max-k_min):
            head = head.next
        k_max_val = head.val
        
        return k_min_val, k_max_val
        
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        n = self.get_list_size(head)
        k = k-1 # make k zero indexed
        k_min = min(k, (n-1)-k)
        k_max = max(k, (n-1)-k)
        k_min_val, k_max_val = self.get_kmin_kmax_vals(head, k_min, k_max)
        
        head2 = head
        for _ in range(k_min):
            head2 = head2.next
        head2.val = k_max_val
        for _ in range(k_max-k_min):
            head2 = head2.next
        head2.val = k_min_val
            
        return head
