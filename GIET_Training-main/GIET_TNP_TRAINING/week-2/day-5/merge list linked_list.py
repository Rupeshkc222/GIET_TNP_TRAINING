'''Write a python function which accepts two linked lists containing integer data and an integer,
n and merges the two linked lists, such that list2 is merged with list1 after n number of nodes.

Assume that value of n will always be less than or equal to the number of nodes in list1.

Sample Input    Expected Output
list1          1-2-4->3->5
list2-          9->8->11
n-2             1->2->9->8->11->4->3->5
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Sll:
    def __init__(self):
        self.head = None
    def traversal(self):
        if self.head is None:
            print("singly linked list is empty")
        else:
            a = self.head
            while a is not None:
                if a.data == 99999:
                    pass
                else:
                    print(a.data, end="->")
                a = a.next
def both_traversal(nn,s1,s2):
    s3 = Sll()
    n4 = Node(99999)
    s3.head = n4
    c = n4
    a=s1.head
    n=0
    b = s2.head
    flag=0
    while a is not None:
        if n<nn:
            c.next=Node(a.data)
            c=c.next
            a=a.next
        n=n+1
        if flag==0 and n==nn:
            while b is not None:
                c.next = Node(b.data)
                c = c.next
                b = b.next
                flag=1
                n=n-2*nn
    s3.traversal()

s1=Sll()
s2=Sll()
l1=[2,4,3,5]
l2=[8,11]
n1=Node(1)
s1.head=n1
c=n1
for i in l1:
    c.next=Node(i)
    c=c.next
s1.traversal()
print()
print("second node")

#for l2
n2=Node(9)
s2.head=n2
c1=n2
for i in l2:
    c1.next=Node(i)
    c1=c1.next
s2.traversal()
print()
print("after merge")
both_traversal(3,s1,s2)