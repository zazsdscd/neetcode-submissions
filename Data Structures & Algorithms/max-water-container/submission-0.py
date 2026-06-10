class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lo,hi = 0, len(heights)-1
        best = 0
        while lo<hi : 
            width = hi - lo
            h = min(heights[lo],heights[hi])
            best = max(h*width,best)
            if heights[lo]<heights[hi]:
                lo+=1
            else :
                hi -=1
        return best
    