'''A teacher has given a project assignment to a class of Students.
She wants to store the marks (out of 100) scored by each student. The marks scored are as mentioned below: 89,78,99,76,77,67,99,98,90
Write a python program to store the marks in a list and perform the following:

1. The teacher forgot to include the marks of one student. Insert 78 at index position, 8 and display the marks of all 10 students.
2. The teacher also wants to know the marks scored by students represented by index positions, 5 and 7.

Identify and display the two marks.'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None

    def traversal(self):
        if self.head is None:
            print("singly linked list is empty")
        else:
            a = self.head
            c=1
            r1=0
            r2=0
            while a is not None:
                if c==5 :
                    r1=a.data
                elif c==7:
                    r2=a.data
                c=c+1
                print(a.data, end=" ")
                a = a.next
            print("value in index 5 is ",r1,"value in index 7 is ",r2)


    def insert_at_any_pos(self,pos,data):
        n=Node(data)
        a=self.head
        for i in range(1,pos-1):
            a=a.next
        n.next=a.next
        a.next=n

sl=sll()
l=[78,99,76,77,67,99,98,90]
n1=Node(89)
sl.head=n1
c=n1
for i in l:
    c.next=Node(i)
    c=c.next
sl.insert_at_any_pos(8,78)    #insert 78 at index position 8
print("the marks of 10 students are:")
sl.traversal()





