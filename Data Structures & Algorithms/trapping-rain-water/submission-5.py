class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        total = 0
        maxL = height[l]
        maxR = height[r]
        while l < r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            h = min(maxL, maxR)
            if height[l] <= height[r]:
                curr = h - height[l]
                if curr > 0:
                    total += curr                    
                l += 1
            else:
                curr = h - height[r]
                if curr > 0:
                    total += curr   
                r -= 1
        
        return total
            
            