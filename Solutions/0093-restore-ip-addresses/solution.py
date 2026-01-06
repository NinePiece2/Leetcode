class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def check_seg(i, j):
            if s[i] == "0" and i != j:
                return False
            return 0 <= int(s[i : j + 1]) <= 255
        
        n = len(s)
        result = []
        tmp = []

        def dfs(i):
            if i >= n and len(tmp) == 4:
                result.append(".".join(tmp))
            if i >= n or len(tmp) == 4:
                return
            for j in range(i, min(i + 3, n)):
                if check_seg(i, j):
                    tmp.append(s[i : j + 1])
                    dfs(j + 1)
                    tmp.pop()
        
        dfs(0)
        return result
