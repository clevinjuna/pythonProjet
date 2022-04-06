from vehicle import Vehicle


# La classe Cat est étendue (extends) de la classe Animal.
class Car(Vehicle):

    def __init__(self, name, brand,speedMax, color, year, typeWheels):
        super().__init__(name, brand, speedMax, color, year)

        self.typeWheels = typeWheels
