class Solution:
    def checkValidString(self, s: str) -> bool:
        minimum, maximum = 0, 0

        for i in range(len(s)):
            if s[i] == '(':
                minimum += 1
                maximum += 1
            elif s[i] == ')':
                minimum -= 1
                maximum -= 1
            # star
            else: 
                minimum -= 1 # ')'
                maximum += 1 # '('

            if maximum < 0:
                return False
            if minimum < 0:
                minimum = 0

        return minimum == 0