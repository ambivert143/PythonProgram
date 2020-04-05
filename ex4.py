car = 100
space_in_a_car = 4.0
drivers = 30
passenger = 90
cars_not_drivers = car - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
averge_passenger_per_car = passenger / cars_driven

print("There are", car, "can available.")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_drivers, "empty car today.")
print("we can transport", carpool_capacity, "people today")
print("we have", passenger, "to carpool today")
print("we need to put about", averge_passenger_per_car, "in each car")