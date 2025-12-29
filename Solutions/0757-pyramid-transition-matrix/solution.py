class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        dic = defaultdict(list)
        for a, b, c in allowed:
            dic[a, b].append(c)
        
        @cache
        def dfs(s: str) -> bool:
            if len(s) == 1:
                return True
            tmp = []
            for a, b in pairwise(s):
                cantidate = dic[a, b]
                if not cantidate:
                    return False
                tmp.append(cantidate)
            
            return any(dfs("".join(next_val)) for next_val in product(*tmp))
        
        return dfs(bottom)

