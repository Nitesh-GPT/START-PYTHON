class Dog:
    def __init__(self, brown, black, white):
        self.brown = brown
        self.black = black
        self.white = white

Dogi = Dog("lovely", "killer", "peaceful")
print(Dogi.brown, Dogi.black, Dogi.white)

Hello = Dog("good", "useless", "nice")
print(Hello.brown, Hello.black, Hello.white)
