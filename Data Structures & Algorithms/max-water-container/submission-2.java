class Solution {
    public int maxArea(int[] heights) {
        int vol = 0,min=0,l=0,r=heights.length-1;
        while(l<r) {
            if(heights[l]<heights[r]) {
                min=heights[l];
            } else {
                min=heights[r];
            }
            if(min*(r-l) > vol) {
                vol = min*(r-l);
            }
            if(heights[l]<heights[r]) {
                l++;
            } else {
                r--;
            }
        }
        return vol;
    }
}
