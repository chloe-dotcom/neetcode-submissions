class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        stack = []

        for i in nums:
            if not stack or i > stack[-1]:
                stack.append(i)
            else:
                l, r = 0, len(stack)-1
                # replace the number just more than i
                while l < r:
                    m = (l+r)//2
                    if i <= stack[m]:
                        r = m
                    else:
                        l = m + 1
                stack[r] = i
        
        return len(stack)
