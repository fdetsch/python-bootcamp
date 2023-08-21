class Device:

    def __init__(self, name, function):
        self.name = name
        self.function = function
    
    def operate(self):
        print('This device is doing stuff.')


class Vacuum(Device):

    def __init__(self, name, function, volume):
        super().__init__(name, function)
        self.volume = volume
    
    def operate(self):
        print(f'The main function of this vacuum cleaner is {self.function}.')


class Kettle(Device):

    def __init__(self, name, function, temperature):
        super().__init__(name, function)
        self.temperature = temperature
    
    def operating_instruction(self):
        print(f'Max. temperature of {self.temperature} can cause severe burning!')
