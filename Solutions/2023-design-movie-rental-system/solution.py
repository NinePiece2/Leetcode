class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.available = defaultdict(lambda: SortedList())
        self.price_hash_map = {}
        for shop, movie, price in entries:
            self.available[movie].add((price, shop))
            self.price_hash_map[self.concat_shop_movie(shop, movie)] = price
        self.rented = SortedList()

    def search(self, movie: int) -> List[int]:
        return [shop for _, shop in self.available[movie][:5]]

    def rent(self, shop: int, movie: int) -> None:
        price = self.price_hash_map[self.concat_shop_movie(shop, movie)]
        self.available[movie].remove((price, shop))
        self.rented.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.price_hash_map[self.concat_shop_movie(shop, movie)]
        self.rented.remove((price, shop, movie))
        self.available[movie].add((price, shop))

    def report(self) -> List[List[int]]:
        return [[shop, movie] for _, shop, movie in self.rented[:5]]

    def concat_shop_movie(self, shop: int, movie: int) -> int:
        return (shop * (2 ** 30)) | movie


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
