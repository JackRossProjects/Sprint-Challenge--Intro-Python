# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]

''' 
class DerivedClassName(BaseClassName):
    pass
'''

#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class
''' The base class is 'vehicle' '''

class Vehicle:
    # This is the base class which other classes will inherit from
    def __init__(self):
        def descrition(self):
            print("I'm a vehicle")

class FlightVehicle(Vehicle):
    pass        

class Airplane(FlightVehicle):
    pass

class Starship(FlightVehicle):
    pass


class GroundVehicle(Vehicle):
    pass

class Car(GroundVehicle):
    pass

class Motorcycle(GroundVehicle):
    pass

vehicle = Vehicle()
ground_vehicle = GroundVehicle()
flight_vehicle = FlightVehicle()
airplane = Airplane()
starship = Starship()
car = Car()
motorcycle = Motorcycle()
