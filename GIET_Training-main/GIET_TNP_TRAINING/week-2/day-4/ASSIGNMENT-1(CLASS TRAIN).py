'''A train is identified by its name and list of compartments.
The compartments are identified by its name,total seating
capacity and the number of passengers.
Implement the class Train as given in the class diagram.
Train
- train_name
- compartment_list
_init_(train_name,compartment_list)
+ get_train_name()
+ get_compartment_list()
+ count_compartments ()
+ check_vacancy()
Write a python program to implement the following:
count_compartments()- returns the total number of compartments
 in the train
check_vacancy()-returns the count of the compartments in which
 more than 50% of the seats are vacant
Note : Compartment list is maintained as a linked list where
data in each node refers to a compartment.

compartment1=Compartment("SL",250,400)
compartment2=Compartment("2AC",125,280)
compartment3=Compartment("3AC",120,300)
compartment4=Compartment("FC",160,300)
compartment5=Compartment("1AC",100,210)
'''

class Compartment:
    def __init__(self,name,nu_of_passenger,total_capacity):
        self.name=name
        self.nu_passenger=nu_of_passenger
        self.t_capacity=total_capacity
        self.next=None
class Train:
    def __init__(self,train_name,compartment_list):
        self.train_name=train_name
        self.first_compartment=compartment_list
    def get_train_name(self):
        return self.train_name
    def get_compartment_list(self):
        compartment_list=[]
        c=self.first_compartment
        while c is not None:
            compartment_list.append(c)
            c=c.next
        return compartment_list
    def count_compartments(self):
        count=0
        a=self.get_compartment_list()
        for i in a:
            count+=1
        return count
    def check_vacancy(self):
        count = 0
        a = self.first_compartment
        while a is not None:
            if a.nu_passenger >= a.t_capacity*0.5:
                count+=1
            a=a.next
        return count


compartment1=Compartment("SL",250,400)
compartment2=Compartment("2AC",125,280)
compartment3=Compartment("3AC",120,300)
compartment4=Compartment("FC",160,300)
compartment5=Compartment("1AC",100,210)
compartment1.next=compartment2
compartment2.next=compartment3
compartment3.next=compartment4
compartment4.next=compartment5

t=Train("Rupesh",compartment1)
print("total number of compartments ",t.count_compartments())
print("total vaccancies above 50 % are ",t.check_vacancy())