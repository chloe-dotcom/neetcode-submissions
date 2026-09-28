class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []

        for i, val in enumerate(nums):
            if not tail or val > tail[-1]:
                tail.append(val)
            
            else:
                l = 0
                r = len(tail) - 1
                # find index of element just greater or equal val
                while l <  r:
                    m = (r+l)//2
                    if val <= tail[m]:
                        r = m
                    else: # val greater, keep searching
                        l = m + 1
                tail[l] = val
            print(tail)
        return len(tail)
                