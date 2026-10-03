class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        z = 0
        t_p = 1
        r = [0] * len(nums) 
        for n in nums:
            if n:
                t_p *=n
            else:
                z +=1
        if z >1:
            return [0] * len(nums)
        for i, n in enumerate(nums):
            if n ==0 and z == 1:
                r[i] = t_p
            elif n and z ==1:
                r[i] = 0
            else:
                r[i] = t_p // n
        return r