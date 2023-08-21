# %% import (function from) module

from car_functions import create_car, drive
import json

cars = []

car = create_car(
    brand = 'Wartburg',
    color = 'white',
    price = 55_000
)

print(json.dumps(car, indent = 2))
drive()

# %% function redefinition

import car_functions as funs

cars = []

# would overwrite `from car_functions import drive`
def drive():
    print('Defined in main program.')

my_car = funs.create_car('BMW', 'red', 35_000, 3)
cars.append(my_car)

print(cars)
drive()
funs.drive()