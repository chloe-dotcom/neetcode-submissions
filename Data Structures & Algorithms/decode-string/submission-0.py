class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        res = ""
        currNum = 0
        for ch in s:
            if ch.isdigit():
                currNum = currNum * 10 + int(ch)
            elif ch == "[":
                stack.append((currNum, res))
                res = ""
                currNum = 0
            elif ch == "]":
                k, ongoingRes = stack.pop()
                res = ongoingRes + (k*res)
            else:
                res += ch
        
        return res