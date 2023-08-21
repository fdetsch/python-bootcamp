# %% user input
name = input('Please enter your name: ')
print(f'Name is {name}')

# input('Press [Enter] to close..')

# %% user input as `int`
## note: input is `string` and needs to be converted to 'int' for arithmetics
x = input('Please enter a number: ')
y = int(x) + 10
print(y)

# %% user input w/ conditional
cars = ['BMW', 'Audi', 'Mercedes', 'Volkswagen', 'Toyota']

user_car = input('Which car are you looking for?')

if user_car in cars:
    print(f'We found a {user_car}.')
else:
    print(f'We could not find a {user_car}.')

# %% exercise

animal = { 'name' : '', 'type' : '', 'age' : 0}

animal['name'] = input('Please enter a name: ')
animal['type'] = input('Please enter a type: ')
animal['age'] = input('Please enter an age: ')

print(f'Meet {animal["name"]}, the {animal["age"]}-year-old {animal["type"]}.')