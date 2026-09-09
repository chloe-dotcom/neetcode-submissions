class Solution:
    def isValid(self, s: str) -> bool:
        matchedParen = {')': '(', ']':'[', '}':'{'}
        stack = []

        for ch in s:
            if ch not in matchedParen:
                stack.append(ch)
                continue
            else:
                if not stack or matchedParen[ch] != stack[-1]:
                    return False
                stack.pop(-1)
        
        return len(stack) == 0