class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        # initialise the stack
        stack = [0]
        for c in S:
            if c == '(':
                # if new paranthesis is open, append a zero to the stack
                stack.append(0)
            else:
                # if paranthesis is closed, retrieve the last element of the stack
                last = stack.pop()
                # if last elem is not zero, the parantesis encapsulated other parantheses, therefore it doubles the value within those parantheses
                stack[-1] += max(1, 2*last)
        return stack[0]
