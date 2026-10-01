class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        stack = []

        for i in nums:
            if not stack or i > stack[-1]:
                stack.append(i)
            else:
                j = 0
                # replace the number just more than i
                while i > stack[j]:
                    j += 1
                stack[j] = i
        
        return len(stack)
