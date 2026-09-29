class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        parts = []
        currNum = 0

        for ch in s:
            if ch.isdigit():
                currNum = currNum * 10 + int(ch)
            elif ch == "[":
                stack.append((currNum, parts))
                parts = []
                currNum = 0
            elif ch == "]":
                k, ongoingRes = stack.pop()
                ongoingRes += (k*("".join(parts)))
                parts = ongoingRes
            else:
                parts.append(ch)
        
        return "".join(parts)