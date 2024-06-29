
class Car:
    def __init__(self, type_of_car, color, gas_tank_capacity=15):
        self.type_of_car = type_of_car
        self.color = color
        self.gas_tank_capacity = gas_tank_capacity
        self.num_gallons = 0

    def paint_job(self, new_color):
        self.color = new_color

    def drive(self, num_miles):
        # assume you lose 1 gallon of gas per mile
        self.num_gallons -= num_miles
        return self.num_gallons

    def fill_up(self, gallons):
        self.num_gallons += gallons
        if self.num_gallons > self.gas_tank_capacity:
            self.num_gallons = self.gas_tank_capacity
        return self.num_gallons

    def get_info(self):
        return self.color + ' ' + self.type_of_car

    def add_capacity(self, new_capacity):
        gas_tank_capacity = new_capacity


#@ @9@ @1@ @20<br>10@ @17<br>7@ @RUNTIME ERROR@
e_type = Car('Jaguar E-Type', 'Black', 17)
print(e_type.fill_up(20))
print(e_type.drive(10))

#@ @9@ @2@ @Red Tesla Roadster<br>Blue Tesla Roadster@ @Red Tesla Roadster<br>Red Tesla Roadster@ @RUNTIME ERROR@
roadster = Car('Tesla Roadster', 'Red', 999)
print(roadster.get_info())
roadster.paint_job('Blue')
print(roadster.get_info())

#@ @9@ @3@ @0<br>-10@ @100<br>90@ @RUNTIME ERROR@
lemon = Car('Lemon', 'Brown', 0)
lemon.add_capacity(1000)
print(lemon.fill_up(100))
print(lemon.drive(10))

