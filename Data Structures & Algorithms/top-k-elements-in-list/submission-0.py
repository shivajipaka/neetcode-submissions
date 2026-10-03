class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        l =[]
        for num in nums:
            if num in d:
                d[num] +=1
            else:
                d[num] =0
        r = [k for k, freq in sorted(d.items(), key=lambda item: item[1], reverse=True)]
        return r[:k]
