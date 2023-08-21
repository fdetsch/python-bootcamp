# %% initialize class

from car import Car

## create instance of class `Car`
my_car = Car('Wartburg', 'white')
my_car.drive()
my_car # prints pointer on disk

my_car.increase_speed(301)
print(f'Max. speed is {my_car.speed} mph.')

my_car1 = Car('BMW', 'black')
my_car1.describe()

my_car1.increase_speed(250)
print(f'Max. speed is {my_car1.speed} mph.')

## append new attribute (not recommended, should happen in class def)
my_car1.noise = 180
print(f'Max. noise is {my_car1.speed} db.')

# %% inheritance

from vehicle import Vehicle, Plane

my_vehicle = Vehicle(180, 5)
print(my_vehicle.door_count)

my_vehicle.drive()

my_plane = Plane(800, 10, 25)
my_plane.start_landing()
print(my_plane.wing_length)

# %% override

from vehicle import Plane

my_plane = Plane(800, 10, 25)
my_plane.drive()

# %% exercise

# Create superclass (parent) 'device' with two subclasses (children)
# Each device has a name and main function
# Some devices have unique properties and functions

from device import Vacuum, Kettle

my_vacuum = Vacuum('T-1000', 'carpet cleaning', '10 liters')
my_vacuum.operate()

my_kettle = Kettle('Boiling Master v1', 'water boiling', '120 degC')
my_kettle.operate()
my_kettle.operating_instruction()