class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # version1_arr, version2_arr = version1.split('.'), version2.split('.')
        # min_len = min(len(version1_arr), len(version2_arr))
        # for i in range(min_len):
        #     if int(version1_arr[i]) == int(version2_arr[i]):
        #         continue
        #     elif int(version1_arr[i]) < int(version2_arr[i]):
        #         return -1
        #     else:
        #         return 1

        # return 0

        m, n = len(version1), len(version2)
        i = j = 0
        while i < m or j < n:
            a = b = 0
            while i < m and version1[i] != '.':
                a = (a * 10) + int(version1[i])
                i += 1
            
            while j < n and version2[j] != '.':
                b = (b * 10) + int(version2[j])
                j += 1
            
            if a != b:
                if a < b:
                    return -1
                else:
                    return 1

            i, j = i + 1, j + 1
        
        return 0
