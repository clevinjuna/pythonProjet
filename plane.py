from vehicle import Vehicle


class Plane(Vehicle):

    def __init__(self, name, brand, speedMax, color, year, typeWings):
        super().__init__(name, brand, speedMax, color, year)

        self.typeWings = typeWings
