class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r = []
        for i, n in enumerate(nums):
            if (target-n) in nums and i != nums.index(target-n):
                j = nums.index(target-n)
                r.append(min(i,j))
                r.append(max(i,j))
                break
        return r