class Solution:
    def validPalindrome(self, s: str) -> bool:
        mary = False
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                if mary:
                    return False
                else:
                    mary = True
                    skipL = s[l+1:r+1]
                    skipR = s[l: r]
                    return skipL == skipL[::-1] or skipR == skipR[::-1]
            
            else:
                l += 1
                r -= 1
        
        return True 