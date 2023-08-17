# %% create dict
persons = [
    { 'name' : 'Jannick', 'height' : 180 },
    { 'name' : 'Peter', 'height' : 190 },
    { 'name' : 'Klara', 'height' : 168 }
]

for person in persons:
    print(f'Name is {person["name"]} and body height is {person["height"]} cm.')

# %% modify dict values

## edit key-value pair
animal = { 'name' : 'Berta', 'type' : 'giraffe' }
animal['type'] = 'lion'

## add new key-value pair
animal['sex'] = 'female'

animal['partner'] = { 'name' : 'Helmut', 'type' : 'giraffe', 'hasChildren': True}

print(animal['partner']['hasChildren'])

# %% delete key-value pairs

## delete pair
animal = { 'name' : 'Berta', 'type' : 'giraffe' }
del animal['type']

banned_users = {
    'Jannick' : False,
    'Peter' : True,
    'Karl' : False
}

## return default if key does not exist (prevents KeyError)
print(banned_users.get('Horst', False)) # default = False

# %% loops and dictionaries

students = [
    { 'name' : 'Jannick', 'age' : 28, 'matricle_no' : 35634},
    { 'name' : 'Peter', 'age' : 30, 'matricle_no' : 24574},
    { 'name' : 'Xenia', 'age' : 21, 'matricle_no' : 99745},
]

for student in students:
    for key, value in student.items():
        print(f'Key: {key}, Value: {value}.')

# %% exercise

# create a list of 5 employees with name, role and salary
# calculate sum of salaries

employees = [
    {
    'name' : 'Anna',
    'role' : 'janitor',
    'salary' : 15_000
    },
    {
    'name' : 'Betty',
    'role' : 'secretary',
    'salary' : 18_500
    },
    {
    'name' : 'Claudia',
    'role' : 'manager',
    'salary' : 42_000
    },
    {
    'name' : 'Andreas',
    'role' : 'clown',
    'salary' : 750
    },
    {
    'name' : 'Jimmy',
    'role' : 'assistant',
    'salary' : 1_500
    }
]

total_salary = 0

for employee in employees:
    total_salary += employee['salary']