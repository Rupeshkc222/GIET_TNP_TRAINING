class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Sll:
    def __init__(self):
        self.head = None
    def traversal(self):
        m = 0
        if self.head is None:
            print("singly linked list is empty")
        else:
            a = self.head
            while a is not None:
                print(a.data, end=" ")
                m=max(m,a.data)
                a = a.next
        return m
    def recheck(self,n,m):
        a = self.head
        while a is not None:
            if a.data==n:
                a.data=m
            a = a.next
s1=Sll()
l1=[11,18,111,100]
n1=Node(1)
s1.head=n1
c=n1
for i in l1:
    c.next=Node(i)
    c=c.next
m=s1.traversal()
s1.recheck(m,98)
print()
print("after change maximum")
s1.traversal()