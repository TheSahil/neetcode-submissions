class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        for i in range(0,len(heights)-1):
            for j in range(i+1,len(heights)):
                m = max((min(heights[i], heights[j]) * (j-i)),m)
                j+=1
            i+=1
        return m