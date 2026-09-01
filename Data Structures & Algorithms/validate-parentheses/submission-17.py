class Solution:
    def isValid(self, s: str) -> bool:
        cl = {')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            if char in cl:
                if not stack or cl[char] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0