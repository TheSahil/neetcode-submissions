class Solution:    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        def sec(nums):
            return nums[1]

        seen = {}
        arr = []
        res = []
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        for s in seen:
            arr.append([s,seen[s]])
        arr.sort(key=sec,reverse=True)
        for i in range(0,k):
            res.append(arr[i][0])
        return res