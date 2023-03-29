'''
Given two queues, one integer queue and another character eue, write a python program to merge them to form a single queue.
Follow the below rules for merging:

Merge elements at the same position starting with the integer queue.

If one of the queues has more elements than the other, add all the additional elements at the end of the output queue.
Note: max_size of the merged queue should be the sum of the size of both the queues. 1

For example,

Input     queue1: 3,6,8   queue2: b,y,u,t,r,o
Output    3,b,6,y,8,u,t,r,o
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
        for index in range(self.front,self.rear+1):
            print(self.element[index])
    def get_max_size(self):
        return self.max_size

def merge_queue(queue1, queue2):
    list1 = []
    list2 = []
    list3 = []

    while (not queue1.is_empty()):
        list1.append(queue1.dequeue())

    while (not queue2.is_empty()):
        list2.append(queue2.dequeue())

    check = 0
    if len(list1) < len(list2):
        length = len(list1)
    else:
        length = len(list2)
        check = 1

    if str(list1[0]).isdigit():
        integer = list1
        string = list2
    else:
        integer = list2
        string = list1
    flag = 0
    j, k = 0, 0
    for i in range(0, 2 * length):
        if flag == 0:
            list3.append(integer[j])
            flag = 1
            j += 1
        elif flag == 1:
            list3.append(string[k])
            flag = 0
            k += 1
    if check == 0:
        for i in list2:
            if i not in list3:
                list3.append(i)
    elif check == 1:
        for i in list1:
            if i not in list3:
                list3.append(i)

    merged_queue = Queue(len(list3))
    for item in list3:
        merged_queue.enqueue(item)
    return merged_queue

# Enqueue different values to both the queues and test your program

queue1 = Queue(3)
queue2 = Queue(6)
queue1.enqueue(3)
queue1.enqueue(6)
queue1.enqueue(8)
queue2.enqueue('b')
queue2.enqueue('y')
queue2.enqueue('u')
queue2.enqueue('t')
queue2.enqueue('r')
queue2.enqueue('o')

merged_queue = merge_queue(queue1, queue2)
print("The elements in the merged queue are:")
merged_queue.display()

'''without queue'''
# q1=[3,6,8]
# q2=['b','y','u','t','r','o']
# res=[]
# min_l=min(len(q1),len(q2))
# for i in range(min_l):
#     res.append(q1[i])
#     res.append(q2[i])
#     if i==len(q1)-1:
#         res=res+q2[i+1:]
#     elif i==len(q2)-1:
#         res=res+q1[i+1:]
# print(res)




'''another way'''
# class queues:
#     def _init_(s,max_size) -> None:
#         s.__max_size=max_size
#         s.__element=[None]*max_size
#         s.__front=0
#         s.__rare=-1
#     def isfull(s):
#         if(s.__rare==s.__max_size-1):
#             return True
#         return False
#     def isempty(s):
#         if(s.__front>s.__rare):
#             return True
#         return False
#     def enqueue(s,val):
#         if(s.isfull()):
#             print("Queue is full")
#         else:
#             s.__rare+=1
#             s.__element[s.__rare]=val
#             # print("inserted {} in the Queue".format(s.__element[s.__rare]))
#     def dqueue(s):
#         if(s.isempty()):
#             print("Queue is empty")
#         else:
#             x=s.__element[s.__front]
#             s.__element[s.__front]=None
#             s.__front+=1
#             # print("Deleted {} in the Queue".format(x))
#             return x
#     def get_max_size(s):
#         return s.__max_size
#     def display(s):
#         # print("The Queue elements are: ",end="")
#         print(','.join([str(s.__element[i]) for i in range(s.__front,s.__rare+1)]))
#         print()
#     def front(s):
#         return s.__element[s.__front]
#
# def merge(q1,q2):
#     s1=q1.get_max_size()
#     s2=q2.get_max_size()
#     q=queues(s1+s2)
#     if(s1>=s2):
#         for i in range(s2):
#             q.enqueue(q1.dqueue())
#             q.enqueue(q2.dqueue())
#         for i in range(s1-s2):
#             q.enqueue(q1.dqueue())
#     else:
#         for i in range(s1):
#             q.enqueue(q1.dqueue())
#             q.enqueue(q2.dqueue())
#         for i in range(s2-s1):
#             q.enqueue(q2.dqueue())
#     q.display()
#
# n=int(input())
# m=int(input())
# q_int=queues(n)
# q_char=queues(m)
# l_int=[q_int.enqueue(int(i)) for i in input().split(',')]
# l_char=[q_char.enqueue(i) for i in input().split(',')]
# merge(q_int,q_char)