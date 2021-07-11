class ChairMixin(object):
    def __init__(self):
        print("is Mixin")
        self.material = "mixin"

    def get_material(self):
        return self.material

    def test(self):
        return("mixin")


class Seat:
    master = "seat"
    def __init__(self):
        print("is Seat")
        self.material = None
        self.height = None
        self.width = None


    def test(self):
        return("Seat")


class Armchair(Seat, ChairMixin):
    def __init__(self):
        super().__init__()
        self.material = "soft"


if __name__ == "__main__":
    simple_armchair = Armchair()
    print(simple_armchair.test())