class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        currNum = 0
        res = ""
        for ch in s:
            if ch.isdigit():
                currNum = currNum * 10 + int(ch)
            elif ch == '[':
                stack.append((currNum, res))
                res = ""
                currNum = 0
            elif ch == ']':
                k, prevRes = stack.pop()
                res = prevRes + (k*res)
            else:
                res += ch
        
        return res