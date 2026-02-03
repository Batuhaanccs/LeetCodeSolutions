class Solution:
    def isValid(self, s: str) -> bool:
        openBrack = ["(","{","["]
        stack = []
        for char in s:
            if char in openBrack:
                stack.append(char)
            elif char == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif char == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif char == "]":
                if not stack or stack.pop() != "[":
                    return False
        if stack == []:
            return True
        return False