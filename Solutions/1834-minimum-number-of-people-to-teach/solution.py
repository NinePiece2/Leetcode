class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        def check_user_langs(u, v) -> bool:
            for x in languages[u - 1]:
                for y in languages[v - 1]:
                    if x == y:
                        return True
            return False

        hash_map = set()
        count = Counter()
        for u, v in friendships:
            if not check_user_langs(u, v):
                hash_map.add(u)
                hash_map.add(v)
        
        for u in hash_map:
            for l in languages[u - 1]:
                count[l] += 1
        
        return len(hash_map) - max(count.values(), default=0)
            
