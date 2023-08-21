# %% function definition

def greet(what = 'world'):
    print(f'Hello, {what}!')

greet() # prints default 'world'
greet('Joe')

# note on parameters vs. arguments
# * 'name' = parameter
# * argument, e.g. 'world', goes in parameter, i.e. 'name'

# %% exercise: append new books to list of books

## global list must be defined outside the function, otherwise not accessible
books = []

def append_book(book):
    books.append(book)

for book in ['Fellowship of the Ring', 'Two Towers', 'Return of the King']:
    append_book(book)

print(books)

# %% multiple parameters

def log_student(name, major):
    print(f'Name of the student is {name} and major subject is {major}.')

log_student('Joe', 'Automotive Engineering') # the order matters!
log_student(major = 'Automotive Engineering', name = 'Joe')

# %% return values

def build_student(name, major = 'Programming'):
    person = {'person_name' : name, 'person_major' : major}
    return person

my_person = build_student('Heiko')
print(f'Person: {my_person}')

def add(x, y):
    result = x + y
    return result

my_result = add(5, 10) # 'my_' prefix to avoid confusion with function object
print(f'Total: {str(my_result)}')

# %% lists as parameters

import json

tracks = [
    {'band' : 'Queen', 'name' : 'Another one bites the dust'},
    {'band' : 'Aerosmith', 'name' : 'Crazy'},
    {'band' : 'Ozzy Osbourne', 'name' : 'Crazy train'},
    {'band' : 'Queen', 'name' : 'The show must go on'},
]

def get_tracks_by_band(band_name, track_list):
    tracks_found = []

    for track in track_list:
        if track['band'] == band_name:
            tracks_found.append(track)
    
    return(tracks_found)

my_tracks_found = get_tracks_by_band('Queen', tracks)
print(json.dumps(my_tracks_found, indent = 2))

# %% exercise

# write a function to assemble a car (dict) and add it to a global list
# call this function 3 times to create 3 different cars
# the car needs a brand, color, price, and # of doors (default 5)

import json

cars = []

def create_car(brand, color, price, n_doors = 5):
    car = {'brand' : brand, 'color' : color, 'price' : price, 'n_doors' : n_doors}
    cars.append(car)

brands = ['VW', 'Hyundai', 'Wartburg']
colors = ['red', 'white', 'blue']
prices = [20_000, 10_000, 55_000]
n_doors = [5, 5, 3]

for brand, color, price, n_doors in zip(brands, colors, prices, n_doors):
    create_car(brand, color, price, n_doors)

print(json.dumps(cars, indent = 2))