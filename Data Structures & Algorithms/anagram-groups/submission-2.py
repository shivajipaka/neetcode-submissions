class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            r = [0] * 26
            for c in s:
                r[ord(c)- ord('a')] +=1
            d[tuple(r)].append(s)
        return list(d.values())