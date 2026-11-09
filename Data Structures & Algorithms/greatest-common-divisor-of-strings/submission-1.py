class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)

        def helper(l):
            if m % l != 0 or n % l != 0:
                return False
            x, y = m//l, n//l
            return str1[:l] * x == str1 and str1[:l] * y == str2 

        for l in range(min(m, n), 0, -1):
            if helper(l):
                return str1[:l]
        
        return ""