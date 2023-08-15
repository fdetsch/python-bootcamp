# %% create lists and append elements

## inconvenient
animal_one = 'monkey'
animal_two = 'goose'

## list of animals
animals = ['monkey', 'goose', 'giraffe', 'rhino']

print(animals[-2:])

## mixed type list
mixed = ['monkey', 3, 4.2]
[print(type(x)) for x in mixed]

# %% sort lists and get length

animals_sorted = sorted(animals)
print(f'Sorted: {animals_sorted}')
print(f'Original: {animals}')

## sort permanently
animals.sort(reverse = False)
print(animals)

## list length
print(f'List length: {len(animals)}')

# %% modify lists

## overwrite single elements
animals[1] = 'elephant'

## append elements to empty list
people = []

people.append('Peter')
people.append('Sarah')

## insert element at n-th position
people.insert(1, 'Hubertus')

## remove elements
removed_person = people.pop() # last element, returns removed element
print(f'Removed person: {removed_person}')

del people[0] # element at n-th position, does not return removed element

animals.remove('elephant') # 1st occurrence only, no return value, i.e. `None`!

# %% exercise:

#1: create an empty list
dishes = []

#2: assign 3 dishes
for dish in ['spaghetti', 'falafel', 'schnitzel']:
    dishes.append(dish)

#3: remove the last element
removed_dish = dishes.pop()

#4: insert a new dish after the 1st element
dishes.insert(1, 'cesar salad')

#5: `print()` the last list element`
print(dishes[-1]) # dishes[len(dishes) - 1]