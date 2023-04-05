'''
Given a queue of numbers. Write a python function to push every second element in the
queue to a stack, if it is the triangle number of the previous element in the
queue and return the stack. The output stack should be of the same size as that of the input queue.

Number d is said to be a triangle number of n, if d = 1+2+3 +.+ (n-2) + (n-1) + n.
For example, 28 is said to be the triangle number of 7, if 1+2+3+4+5+6+7 is equal to 28.

Sample Input                                     Expected Output

Input queue (front->rear):                      Output stack ( top->bottom):
 7,28,8,35,3,6,5,15,2,5                         15,6,28
 '''
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
        q.create_stack()
        c=0
        l=[]
        for index in range(self.front,self.rear+1):
            print(self.element[index],end=' ')
            num=self.element[index]
            s=0
            if index<self.rear-1:
                while num > 0:
                    s = s + num
                    num -= 1
                if self.element[index + 1] == s:
                    q.push(self.element[index+1])
        return self.stack
    def create_stack(self):
        self.stack = []
        return self.stack

    def push(self,item):
        self.stack.append(item)
    # def pop_it(self):
    #     for i in self.stack:
    #         print(self.stack.pop())

l=[7,28,8,35,3,6,5,15,2,5]
s=len(l)
q=Queue(s)
for i in l:
    q.enqueue(i)
r=q.display()
print("printing of stack")
print(r[::-1])
