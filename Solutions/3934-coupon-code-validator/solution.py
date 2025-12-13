class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        pattern = r"^[a-zA-Z0-9_]+$"
        valid_bussiness = {"electronics", "grocery", "pharmacy", "restaurant"}
        valid_index = []
        for i, (c, bussiness, active) in enumerate(zip(code, businessLine, isActive)):
            if active and re.fullmatch(pattern, c) and bussiness in valid_bussiness:
                valid_index.append(i)
        valid_index.sort(key=lambda x: (businessLine[x], code[x]))
        print(valid_index)
        return [code[val] for val in valid_index]
