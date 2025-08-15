class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for stri in strs:
            curr = ''.join(sorted(stri))
            dic[curr].append(stri)

        return list(dic.values())
