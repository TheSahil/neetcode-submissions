class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prd = 1
        suf = []
        pre = []
        res = []

        s = 1
        p = 1
        
        for i in range(len(nums)-1,-1,-1):
            suf.append(s)
            s *= nums[i]

        suf.reverse()
        
        for i in range(0,len(nums)):
            pre.append(p)
            p *= nums[i]
            res.append(pre[i]*suf[i])
        
        print(pre)
        print(suf)
        return res