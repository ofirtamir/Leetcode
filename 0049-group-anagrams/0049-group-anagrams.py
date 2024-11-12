class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # dic = {}
        # for s in strs:
        #     x = tuple(sorted(s))
        #     if x not in dic:
        #         dic[x] = [s]
        #     else:
        #         dic[x].append(s)
                
        # return list(dic.values())


        dic = defaultdict(list)
        for x in strs:
            h = [0] * 26
            for y in x :
                h[ord(y)- ord('a')] += 1
            dic[tuple(h)].append(x)
        return list(dic.values())

