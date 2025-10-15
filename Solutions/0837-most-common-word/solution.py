class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_Set = set(banned)
        count = Counter(re.findall("[a-z]+", paragraph.lower()))
        return next(word for word, _ in count.most_common() if word not in banned_Set)
