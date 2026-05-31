class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for num in nums:
            s.add(num)
        print(s)

        maxLen = 0

        for num in nums:
            if num-1 not in nums:
                l = 1
                i = num
                while(i+1 in nums):
                    l+=1
                    i+=1
                if l>maxLen:
                    maxLen = l
        print(maxLen)
        return maxLen