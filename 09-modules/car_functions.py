def create_car(brand, color, price, n_doors = 5):
    car = {'brand' : brand, 'color' : color, 'price' : price, 'n_doors' : n_doors}
    return car

def drive():
    print('The car is driving.')