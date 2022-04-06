from vehicle import Vehicle


class Bike(Vehicle):

    def __init__(self, name, brand, speedMax, color, year, typeMotor):
        super().__init__(name, brand, speedMax, color, year)

        self.typeMotor = typeMotor
