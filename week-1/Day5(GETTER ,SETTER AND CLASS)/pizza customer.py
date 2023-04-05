# # PizzaForYou is a pizza store which sells different kinds of pizzas based on customer's order.40 min
# Customer can either collect the order in person or opt for a door delivery.
# Write a python program based on the class diagram given below.
# Customer class:
# validate_quantity(): A customer can order 1 to 5 pizzas
# If quantity is valid, return true. Else return false

# Pizzaservice class:
# Initialize static variable counter to 100
# Attribute, additional_topping is a boolean value which indicates whether additional topping is required or not.
# True – additional topping is required, False – additional topping is not required
# validate_pizza_type(): Customers can order "small" or "medium" type pizzas
# If pizza type is valid, return true. Else return false
# calculate_pizza_cost(): Calculate pizza cost
# Validate pizza type and quantity
# If valid,
# Identify pizza cost based on details mentioned in the table
# Set attribute, pizza_cost with the calculated pizza cost
# Auto-generate service_id starting from 101 prefixed by first letter of pizza type. Example – S101, s102, m103, S104, M105 etc
# If invalid, set pizza_cost to -1
# PizzaType	                Cost/Pizza(in Rs)	        Additional topping cost/Pizza (in Rs), if applicable
# Small	                            150	                                        35
# Medium	                        200	                                        50

# Doordelivery class:
# validate_distance_in_kms(): Minimum distance for door delivery is 1km and maximum is 10kms
# Validate distance_in_kms
# If valid, return true. Else, return false
# calculate_pizza_cost: Calculate pizza cost
# Validate distance in kms
# If valid,
# Calculate pizza cost (Hint: Invoke overridden method in parent class)
# If pizza_cost is not -1, identify delivery charge based on details mentioned below and add it to attribute, pizza_cost
# Distance in kms	Delivery Charge in km(in Rs)
# For first 5 kms	5
# For remaining 5 kms	7
# Else, set pizza_cost to -1
# Note: Perform case insensitive string comparison
# For testing:
# Create objects of Pizzaservice and Doordelivery classes
# Invoke calculate_pizza_cost() on Pizzaservice and Doordelivery objects
# Display the detail


class customer:
    def __init__(self):
        self.__quantity=None
    def validate_quantity(self,quantity):
        self.__quantity=quantity
        if self.__quantity>0:
            return True
        else:
            return False
class Pizzaservice:
    def __init__(self):
        self.__pizza_type=None
        self.__quantity=None
        self.__add_toping=None
    def validate_pizza_type(self,pizza_type,quantity,add_toping):
        self.__pizza_type=pizza_type
        self.__quantity=quantity
        self.__add_toping=add_toping
        l=[]
        id=""
        num=100
        if (self.__pizza_type =="Small" or self.__pizza_type=="Medium") :
            a=self.__pizza_type[0]
            if a=='S' or a=='M':
                id=a+str(num)
                self.__quantity_price=150*self.__quantity
                if self.__add_toping >1:
                    self.__quantity_price=self.__quantity_price+self.__add_toping*35
            l.append([id,self.__quantity_price])
            num=num+1
        else:
            l.append([0,0])
        return l

class Door_Deliver:
    def _init_(self):
        self.__d=None
        self.__pc=None
    def pizza_cost_door(self,dis,pizza_cost):
        self.__d = dis
        self.__pc = pizza_cost
        if(self.__d <6):
            self.__pc=self.__pc+(self.__d*5)
            return self.__pc
        elif(self.__d>=6):
            self.__pc=self.__pc+((self.__d-5)*7)+(self.__d*5)
            return self.__pc

v1=customer()
q=int(input("enter the quantity"))
v1_sol=v1.validate_quantity(q)
print("VERIFY",v1_sol)
if v1_sol==True:
    v2=Pizzaservice()
    v2_sol=v2.validate_pizza_type("Small",q,3)
    print("ID    AND    AMOUNT QUANTITY AFTER TOPING",v2_sol)
else:
    print(-1)
# print(v2_sol[0][1])
distance=int(input("ENTER DISTANCE"))
if v2_sol[0][1]!=0 and distance>1:
    v3=Door_Deliver()
    v3_sol=v3.pizza_cost_door(distance,v2_sol[0][1])
    print("COST OF PIZZA ACCORDING TO DISTANCE",v3_sol)
else:
    print("not valid distance")
