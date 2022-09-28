class Anime:
    def __init__(self, name):
        self.name = name
        # raise exception if not string?
        self.rating = 1000

    def __str__(self):
        return f"{self.name}, rating: {self.rating}"

anime_a = Anime("jjk")
anime_b = Anime("chainsaw man")

print(anime_a)