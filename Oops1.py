#creating an Cat class where name and address are initiated these two property are  inside the def fucnction,
class Cat:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        print(name, address)

caty = Cat("nitesh", "gorakhpur")
print(caty.name)
print(caty.address)
