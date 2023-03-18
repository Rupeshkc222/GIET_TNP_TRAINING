# WeCare insurance company wants to calculate premium of vehicles.
# -->Vehicles are of two types - "Two Wheeler" and "Four Wheeler" Each vehicle is identified by
# vehicle id, type, cost and premium amount.
# -->Premium amount is 2% of the vehicle cost for two wheelers and6% of the vehicle cost for four wheelers.
#
# Calculate the premium amount and display the vehicle details. Write a Python program to implement the class chosen
# with its attributes and methods.
#
# Note:Consider all instance variables to be private and methods to be public
# Include getter and setter methods for all instance variables) Display appropriate error message, if the vehicle type is invalid.
# Perform case sensitive string comparison Represent few objects of the class,
# initialize instance variables using setter methods, invoke appropriate methods and test your program.

class vehicle:
    def __init__(self):
        self.__vehicle_id=None
        self.__vehicle_cost = None
        self.__vehicle_type = None
        self.__vehicle_premium = None

    def set_vehcile_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
    def set_vehcile_type(self,vehicle_type):
        self.__vehicle_type=vehicle_type
        if vehicle_type=="Two Wheeler" or vehicle_type=="four Wheeler":
            self.__vehicle_type=vehicle_type
        else:
            return "invalid vechile name given"
    def set_vehcile_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
    def set_vehcile_premium(self,vehicle_premium):
        self.__vehicle_premium=vehicle_premium
    def get_vehcile_id(self):
        return self.__vehicle_id
    def get_vehcile_type(self):
        return self.__vehicle_type
    def get_vehcile_cost(self):
        return self.__vehicle_cost
    def calculate_premium(self):
        if self.__vehicle_type == "Two Wheeler":
            self.__vehicle_premium=self.__vehicle_cost*0.02
        elif self.__vehicle_type == "four Wheeler":
            self.__vehicle_premium=self.__vehicle_cost*0.06
    def get_vehcile_premium(self):
        return self.__vehicle_premium

    def display_vehicle_details(self):
        print(self.__vehicle_id,self.__vehicle_type, self.__vehicle_cost, int(self.__vehicle_premium))

v1 = vehicle()
v1.set_vehcile_id(input())
v1.set_vehcile_type(input())
v1.set_vehcile_cost(int(input()))
v1.calculate_premium()
v1.display_vehicle_details()