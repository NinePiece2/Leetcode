class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # result = 0
        # for j in range(len(strs[0])):
        #     for i in range(1, len(strs)):
        #         if strs[i - 1][j] > strs[i][j]:
        #             result += 1
        #             break
        # return result
        return(sum(col!=sorted(col) for col in map(list, zip(*strs))))
