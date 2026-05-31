class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = {}
        result = []

        for i in range(0,len(strs)):
            if(''.join(sorted(strs[i])) in seen):
                seen[''.join(sorted(strs[i]))].append(i)
            else:
                seen[''.join(sorted(strs[i]))] = [i]

        # print(seen)

        for item in seen:
            tempRes = []
            print(item)
            for i in seen[item]:
                tempRes.append(strs[i])
            result.append(tempRes)

        return result