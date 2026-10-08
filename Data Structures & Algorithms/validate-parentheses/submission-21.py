class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')':'(', '}':'{', ']':'['}
        stack = []
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack:
                    return False
                if stack.pop() != closeToOpen[ch]:
                    return False
        
        return len(stack) == 0