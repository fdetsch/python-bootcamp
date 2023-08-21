# %% basics

counter = 0

while counter < 5:
    counter += 1 # not increasing counter would result in endloss loop

print(counter)

# %% remove elements from `list`

cars = ['BMW', 'Audi', 'BMW', 'Mercedes', 'BMW', 'Toyota']

while 'BMW' in cars:
    cars.remove('BMW') # removes 1st occurrence of value

print(cars)

# %% program lifecycle

print('Welcome to my lecture. Please present yourselves shortly.')

students = []
user_input = ''

while user_input != 'quit':
    user_input = input("What's your name?")

    if (user_input != 'quit'):
        print(f'Hello, {user_input}!')
        students.append(user_input)

print(', '.join(students) + " - that's all, let's begin!")

# %% break statement

print('Even or Odd')

user_input = ''

while True:

    user_input = input('Please enter a number: ')

    if user_input == 'quit':
        print("Goodbye.")
        break
    else:
        digit = int(user_input)

        if digit % 2 == 0:
            print(f'Number is even.')
        else:
            print(f'Number is odd.')

# %% exercise

## write a program that takes employee and salary as user input
## save these to a list
## return the full list

import json

employees = []

while True and len(employees) < 3:

    name = input("What's the name of the employee.")
    if name == 'quit':
        break

    salary = input("What's the salary?")
    if salary == 'quit':
        break

    employee = {}
    employee[name] = salary
    employees.append(employee)

print(json.dumps(employees, indent = 2))
