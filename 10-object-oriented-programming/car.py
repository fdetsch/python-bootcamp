class Car:

    # not mandatory, but useful when assigning values upon initialization
    def __init__(self, brand, color, speed = 180):
        self.brand = brand
        self.color = color
        self.speed = speed
        print(f'Initializing a {color} {brand} ..')
    
    # note: a function associated with a class is called 'method'
    def increase_speed(self, new_value):
        if new_value > 300:
            print('This is too fast, retaining current speed.')
            return # break current function if condition is met
        
        self.speed = new_value
    
    def drive(self):
        print(f'The {self.color} {self.brand} is driving.')
    
    def describe(self):
        print(f'The car is brand {self.brand} and has color {self.color}.')