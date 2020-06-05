# Class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]

# Base class
class Vehicle:
    pass 

# Vehicle -> FlightVehicle
class FlightVehicle(Vehicle):
    pass 

# Vehicle -> GroundVehicle
class GroundVehicle(Vehicle):
    pass 

# Vehicle -> FlightVehicle -> Starship
class Starship(FlightVehicle):
    pass 

# Vehicle -> FlightVehicle -> Airplane
class Airplane(FlightVehicle):
    pass 

# Vehicle -> GroundVehicle -> Car
class Car(GroundVehicle):
    pass 

# Vehicle -> GroundVehicle -> Motorcycle
class Motorcycle(GroundVehicle):
    pass 