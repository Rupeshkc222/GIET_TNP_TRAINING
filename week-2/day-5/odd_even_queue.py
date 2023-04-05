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
            print("jqueue is full")
        else:
            self.rear+=1
            self.element[self.rear]=data
    def display_even_odd(self):
        for index in range(self.front,self.rear+1):
            print(self.element[index],end=" ")
    def display(self):
        o=0
        e=0
        l=[]
        for index in range(self.front,self.rear+1):
            print(self.element[index])
            l.append(self.element[index])
            if self.element[index] %2==0:
                e=e+1
            else:
                o=o+1
        oq=Queue(e)
        oe=Queue(o)
        for i in l:
            if i%2==0:
                oq.enqueue(i)
            else:
                oe.enqueue(i)
        print("even queue")
        oq.display_even_odd()
        print()
        print("odd queue")
        oe.display_even_odd()
    def get_max_size(self):
        return self.max_size
q=Queue(7)
print("it is full",q.is_full())
print("it is empty",q.is_empty())
q.enqueue(2)
q.enqueue(7)
q.enqueue(9)
q.enqueue(4)
q.enqueue(6)
q.enqueue(5)
q.enqueue(10)
q.display()