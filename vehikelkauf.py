order = []

# What does the client want at all?
vehicle = input('Choose a vehicle (car, aircraft, boat): ')
order.append(vehicle)

vehicle = vehicle.lower()

if vehicle == 'car':
    brand = input('Choose a brand (Audi, BMW, VW): ')
    order.append(brand)

    brand = brand.lower()

    if brand == 'audi':
        answer = 'Great choice!'
    elif brand == 'bmw':
        answer = 'Go out and buy an Audi!'
    elif brand == 'vw':
        answer = 'Go out and buy an Audi!'
    else:
        answer = 'Buy yourself a gscheid`s car'
elif vehicle == 'aircraft':
    brand = input('Choose a brand (Airbus, Cessna, Boeing): ')
    if brand.lower() in ('airbus', 'cessna', 'boeing'):
        order.append(brand)
        answer = 'Great choice!'
    else:
        answer = 'No such aircraft: ' + brand
elif vehicle == 'boat':
    answer = 'Buy a car and try again!'
else:    
    answer = 'What do you think you are doing here?'

print('Hey You!', answer)

print('Order:', order)
