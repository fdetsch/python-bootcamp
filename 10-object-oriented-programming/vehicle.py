class Vehicle:

    def __init__(self, max_speed, door_count):
        self.max_speed = max_speed
        self.door_count = door_count
    
    def drive(self):
        print('The vehicle is driving.')


class Plane (Vehicle):

    # inherits `__init__()` from super class if not defined
    def __init__(self, max_speed, door_count, wing_length):
        super().__init__(max_speed, door_count)
        self.wing_length = wing_length
    
    def start_landing(self):
        print('The airplane begins to land.')
    
    # override `drive` method from superclass
    def drive(self):
        print('The plane flies.')
