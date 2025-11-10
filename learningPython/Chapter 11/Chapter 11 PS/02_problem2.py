class Animals():
    pass

class Pets(Animals):
    pass

class Dogs(Pets):
    @staticmethod
    def bark():
        print("Woof!")

d = Dogs()
d.bark()