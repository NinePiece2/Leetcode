class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def remove_vowel(word):
            return "".join('*' if char in "aeiou" else char for char in word)

        correct_words = set(wordlist)
        words_capital = {}
        words_vowel = {}

        for word in wordlist:
            lower_word = word.lower()
            words_capital.setdefault(lower_word, word)
            words_vowel.setdefault(remove_vowel(lower_word), word)

        result = []
        for query in queries:
            if query in correct_words:
                result.append(query)
                continue

            query = query.lower()
            if query in words_capital:
                result.append(words_capital[query])
                continue

            query = remove_vowel(query)
            if query in words_vowel:
                result.append(words_vowel[query])
                continue
            
            result.append("")
        return result
            
