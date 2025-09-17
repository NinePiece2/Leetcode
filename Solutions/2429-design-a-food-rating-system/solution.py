class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.dict = defaultdict(SortedList)
        self.hash_table = {}
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.dict[cuisine].add((-rating, food))
            self.hash_table[food] = (rating, cuisine)

    def changeRating(self, food: str, newRating: int) -> None:
        rating, cuisine = self.hash_table[food]
        self.hash_table[food] = (newRating, cuisine)
        self.dict[cuisine].remove((-rating, food))
        self.dict[cuisine].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.dict[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
