class Queue:
    def __init__(self,max_size):
        self.max_size=max_size
        self.element=[None]*self.max_size
        self.rear=-1
        self.front=0
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
    def dequeue(self):
        if self.is_empty():
            print("queue is empty")
        else:
            data=self.element[self.front]
            self.front+=1
            return data
    def display(self):
        for index in range(self.front,self.rear+1):
            print(self.element[index])
    def get_max_size(self):
        return self.max_size
q=Queue(4)
print("it is full",q.is_full())
print("it is empty",q.is_empty())
q.enqueue(100)
q.display()
q.enqueue(200)
q.enqueue(400)
q.enqueue(300)
q.enqueue(900)
q.enqueue(700)
q.display()
q.enqueue(500)
q.display()
print("element deleted",q.dequeue())
q.display()



