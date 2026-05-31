class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        seen = set()
        if(len(s) == 0):
            return 0
        seen.add(s[0])
        maxLen = 1
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            tempMax = r - l + 1
            maxLen = max(maxLen, tempMax)
            r += 1
        return maxLen

