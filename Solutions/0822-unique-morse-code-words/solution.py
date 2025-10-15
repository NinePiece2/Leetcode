class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                    "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
                    "..-","...-",".--","-..-","-.--","--.."]
        # morse_set = set()
        # for word in words:
        #     morse_code = ""
        #     for char in word:
        #         morse_code += morse[ord(char) - ord('a')]
        #     if morse_code not in morse_set:
        #         morse_set.add(morse_code)

        # return len(morse_set)
        morse_set = {"".join([morse[ord(char) - ord('a')] for char in word]) for word in words}
        return len(morse_set)
