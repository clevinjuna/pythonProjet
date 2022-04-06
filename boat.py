from vehicle import Vehicle


class Boat(Vehicle):

    def __init__(self, name, brand, speedMax, color, year, typeHull):
        super().__init__(name, brand, speedMax, color, year)

        self.typeHull = typeHull
