class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            x = tuple(sorted(s))
            if x not in dic:
                dic[x] = [s]
            else:
                dic[x].append(s)
                
        return list(dic.values())
        