class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i, n = 0, len(words)

        while i < n:
            temp = []
            count = len(words[i])
            temp.append(words[i])
            i += 1
            while i < n and (count + 1 + len(words[i])) <= maxWidth:
                count += 1 + len(words[i])
                temp.append(words[i])
                i += 1

            if i == n or len(temp) == 1:
                left = ' '.join(temp)
                right = ' ' * (maxWidth - len(left))
                result.append(left + right)
                continue
            
            space_width = maxWidth - (count - len(temp) + 1)
            val, remain = divmod(space_width, len(temp) - 1)

            row = []
            for index, word in enumerate(temp[:-1]):
                row.append(word)
                row.append(' ' * (val + (1 if index < remain else 0 )))

            row.append(temp[-1])
            result.append(''.join(row))

        return result

