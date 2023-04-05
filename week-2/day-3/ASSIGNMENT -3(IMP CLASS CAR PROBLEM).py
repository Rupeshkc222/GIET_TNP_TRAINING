'''consider a Car class as given in the code. Write a Service ass as given in the class diagram below which performs
various activities on a list of cars.

Assume that the car_list is sorted by year in ascending order.
Service:
car_list
init(car_list)
+get_car_list()
+find_cars_by_year (year)
+add_cars (new_car_list)
+remove_cars_from_karnataka()
Method Description

init(car_list)

--Initializes the instance variable, car_list..

second method:
Description

hit_(car_list)

-Initializes the instance variable, car_list.

find_cars_by_year (year) ----Finds and returns the list of models of all the cars with the year as the one passed as the argument. If there are

add_cars (new_car_list)

--The new_car_list should be added to the instance variable car_list.

The car list should be still sorted such that the years are in ascending order.
remove_cars_from_karnataka()
Finds and removes all cars with registration number beginning with "KA" from the car_list.
'''
class Car:
    def _init_(self, model, year, registration_number):
        self.model = model
        self.year = year
        self.registration_number = registration_number

class Service:
    def _init_(self, car_list):
        self.car_list = car_list

    def get_car_list(self):
        return self.car_list

    def find_cars_by_year(self, year):
        return [car for car in self.car_list if car.year == year]

    def add_cars(self, new_car_list):
        self.car_list.extend(new_car_list)
        self.car_list.sort(key=lambda car: car.year)

    def remove_cars_from_karnataka(self):
        self.car_list = [car for car in self.car_list if not car.registration_number.startswith("KA")]

# Create some Car objects and a list of Car objects
car1 = Car("Audi", 2010, "KA01AB1234")
car2 = Car("BMW", 2011, "MH02CD4567")
car3 = Car("Mercedes", 2012, "KA03EF8901")
car_list = [car1, car2, car3]

# Create a Service object and call some methods on it
service = Service(car_list)
print(service.get_car_list())

new_car_list = [Car("Tesla", 2020, "KA04GH5678"), Car("Toyota", 2022, "MH05IJ9012")]
service.add_cars(new_car_list)
print(service.get_car_list())

print(service.find_cars_by_year(2011))

service.remove_cars_from_karnataka()
print(service.get_car_list())


