'''
Write a python program to remove all duplicate elements from a sorted linked list containing integer data.
Use the LinkedList class and methods in it to implement the above program.

Example:

Input LinkedList: 10 10 20 20 30 30 30 40 50
Output LinkedList: 10 20 30 40 50
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class sll:
    def __init__(self):
        self.head=None
    def traversal(self):
        if self.head is None:
            print("linked list is empty")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=" ")
                a=a.next
    def up_date(self):
        if self.head is None:
            print("linked list is empty")
        else:
            a=self.head
            while a.next is not None:
                if a.data==a.next.data:
                    a.next=a.next.next
                else:
                    a=a.next


n=[10,20,20,30,30,30,40,50]
s=sll()
n1=Node(10)
s.head=n1
c=n1
for i in n:
    c.next=Node(i)
    c=c.next
print("before sorting")
s.traversal()
print()
print("after sorting")
s.up_date()
s.traversal()