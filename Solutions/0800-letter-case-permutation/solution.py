class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # result = []
        # n = sum(char.isalpha() for char in s)

        # for i in range(1 << n):
        #     j, tmp = 0, []
        #     for char in s:
        #         if char.isalpha():
        #             char = char.lower() if (i >> j) & 1 else char.upper()
        #             j += 1
        #         tmp.append(char)
        #     result.append("".join(tmp))

        # return result

        result = [""]
        for char in s:
            if char.isdigit():
                result = [rchar + char for rchar in result]
            else:
                result = [rchar + val for rchar in result for val in (char.upper(), char.lower())]
        
        return result
