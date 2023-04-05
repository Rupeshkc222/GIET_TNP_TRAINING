'''Given a queue of whole numbers. Write a python function to return a new queue which contains the evenly divisible numbers.
Note: A number is said to be evenly divisible if it is divisible by all the numbers in the given range without any remainder.
Consider the range to be from 1 to 10 (both inclusive).
Assume that there will always be few elements in the input queue, which are evenly divisible by the numbers in the mentioned range.

Example:

Input Queue: 13983, 10080, 7113, 2520, 2500 (front - rear)

Output Queue: 10080, 2520 (front-rear)'''

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
        for index in range(self.front, self.rear + 1):
            print(self.element[index])
    def get_max_size(self):
        return self.max_size
n = int(input())

ipq=Queue(n)
print("it is full",ipq.is_full())
print("it is empty",ipq.is_empty())
for i in range(n):
    ipq.enqueue(int(input()))
print("SO THE CORRECT QUEUE IS ")
opq = Queue(10)
for i in range(n):
    ele = ipq.dequeue()
    cnt=0
    for i in range(1,11):
        if ele%i==0:
            cnt+=1
    if cnt==10:
        opq.enqueue(ele)
opq.display()

