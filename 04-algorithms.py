# %% `for` loops

cars = ['Audi', 'BMW', 'Volkswagen', 'Mercedes']

## iterate over cars
n = 0

for car in cars:
    n += 1
    print(f'Car #{n} is {car}.')

# note the 1st non-indented line after `for` loop is the end of `for` loop

# %% exercise: `for` loops

## print stundents in 2 separate classes
class_a = ['Jan', 'Nick', 'Maria', 'Peter']
class_b = ['Klara', 'Jonas', 'Hans', 'Vladimir']

for student_a, student_b in zip(class_a, class_b):
    print(f'{student_a}, {student_b}')

## or append students from class b to class a
classes = class_a.copy()

for student_b in class_b:
    classes.append(student_b)

print(classes)

# %% lists containing numbers

digits = list(range(1, 6))

smallest_digit = min(digits)
highest_digit = max(digits)
result = sum(digits)

print(f'Min: {smallest_digit}, Max: {highest_digit}, Sum: {result}')

# %% if-else

age = 4

if age >= 6 and age <= 60: # `if`: keyword, `==`: operator
    print('Regular.')
elif age < 6:
    print('Reduced (child).')
else:
    print('Reduced (senior).')


# %% value contained in `list`

cities = ['Berlin', 'Madrid', 'Paris']

if 'Dortmund' in cities:
    print('Is contained.')
else:
    print('Not contained.')


# %% example:

revenues = [1000, 2000, 3000, 2500, 1500, 800, 2200, 2600, 3000, 2100, 2000, 1800]

total_best_months = 0
total_count_best_month = 0

for revenue in revenues:
    if revenue >= 2000:
        total_best_months += revenue
        total_count_best_month += 1

print(f'Total of best months ({total_count_best_month}): {total_best_months}€')

# %% exercise

# create `list` with 10.000 values (1-10.000)
# create two empty `list` objects (list_a and list_b)

# for each value in `list` investigate if divisible by 5
# true -> append value to list_a
# false -> append -"- list_b
values = list(range(1, 10_001)) # underscore removed afterwards
list_a = []
list_b = []

for value in values:
    if value % 5 == 0:
        list_a.append(value)
    else:
        list_b.append(value)