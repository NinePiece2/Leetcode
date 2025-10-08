class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n, m = len(spells), len(potions)
        result = [m - bisect_left(potions, success / val) for val in spells]
        return result

        # potions.sort()
        # n, m = len(spells), len(potions)
        # result = []
        # for i in range(n):
        #     left, right = 0, m - 1
        #     index = m

        #     while right >= left:
        #         mid = (left + right) // 2
        #         if spells[i] * potions[mid] >= success:
        #             index = mid
        #             right = mid - 1
        #         elif spells[i] * potions[mid] < success:
        #             left = mid + 1
        #     result.append(m - index)

        # return result
