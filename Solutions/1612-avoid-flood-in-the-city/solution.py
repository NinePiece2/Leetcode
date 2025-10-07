class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        result = [1] * len(rains)
        dry = SortedList()
        rainy = {}

        for i, val in enumerate(rains):
            if val ==0 :
                dry.add(i)
            else:
                result[i] = -1
                if val in rainy:
                    index = dry.bisect_left(rainy[val])
                    if index == len(dry):
                        return []
                    result[dry[index]] = val
                    dry.discard(dry[index])
                rainy[val] = i
        
        return result
