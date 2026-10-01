class Solution:
    def decodeString(self, s: str) -> str:
        self.i = 0

        def helper():
            res = ""
            k = 0
            while self.i < len(s):
                ch = s[self.i]
                if ch.isdigit():
                    k = k*10 + int(ch)
                elif ch == '[':
                    self.i+=1
                    res += k * helper()
                    k = 0
                elif ch == ']':
                    return res
                else:
                    res += ch
                self.i += 1
            return res
        
        return helper()