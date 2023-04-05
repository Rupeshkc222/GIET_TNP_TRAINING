class Queue:
    def __init__(self,max_size):
        self.max_size=max_size
        self.element=[None]*self.max_size
        self.rear=-1
        self.front=0

    def details(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def is_full(self):
        if self.rear==self.max_size-1:
            return True
        return False
    def is_empty(self):
        if self.front>self.rear:
            return True
        return False
    def enqueue(self,data):
        if self.is_full():
            print("Queue is full")
        else:
            self.rear+=1
            self.element[self.rear]=data
    def display(self):
        for index in range(self.front,self.rear+1):
            print(self.element[index])
    def find_gender_details(self,g):
        for index in range(self.front, self.rear + 1):
            if self.element[index][2] ==g:
                print(self.element[index])


q=Queue(4)
q.enqueue(["Alice", 25, "female"])
q.enqueue(["Bob", 30, "male"])
q.enqueue(["Charlie", 35, "male"])
q.enqueue(["Deborah", 40,"female"])
q.display()
to_find="male"
print("display the ",to_find)
q.find_gender_details(to_find)