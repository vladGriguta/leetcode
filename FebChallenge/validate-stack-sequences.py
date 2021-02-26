class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # idea: re-create the push-pop operations and apply pop at each step it is allowed
        stack = []
        for el in pushed:
            # append each element to the stack
            stack.append(el)
            # while last element of the stack was popped
            # delete the element from the stack and from the popped list
            while stack and stack[-1]==popped[0]:
                stack.pop()
                popped.pop(0)
        
        # if stack is empty, all pushed elements were popped
        return not stack
