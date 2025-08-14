class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = Counter()
        for d in cpdomains:
            val = int(d[: d.index(' ')])
            for i, ch in enumerate(d):
                if ch in ' .':
                    count[d[i + 1: ]] += val
            
        result = [f'{val} {domain}' for domain, val in count.items()]
        return result
