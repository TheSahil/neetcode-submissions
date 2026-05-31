class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(0,len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for v, c in count.items():
            freq[c].append(v)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                if len(res) < k:
                    res.append(j)
        return res