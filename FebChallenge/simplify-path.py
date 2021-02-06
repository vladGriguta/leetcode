class Solution:
    def simplifyPath(self, path: str) -> str:
        # iterate through the strings between the `/` character
        stack, tokens = [], path.split("/")
        for token in tokens:
            if token == ".." and stack:
                stack.pop()
            elif token != ".." and token != "." and token:
                stack.append(token)
        return "/" + "/".join(stack)
                        