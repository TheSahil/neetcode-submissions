class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        result = []
        for i in range(0,len(nums)):
            if target-nums[i] in seen and seen.get(target-nums[i]) != i:
                result.append(seen.get(target-nums[i]))
                result.append(i)
                exit
            seen[nums[i]] = i
        return result
            