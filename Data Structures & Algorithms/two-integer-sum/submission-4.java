class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> n = new HashMap<Integer,Integer>();
        for(int i=0;i<nums.length;i++) {
            if(n.containsKey(target-nums[i])) {
                int[] r = {n.get(target-nums[i]),i};
                return r;
            }
            n.put(nums[i],i);
        }
        return null;
    }
}
