'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Dll:
    def __init__(self):
        self.head=None
    def forward_traversal(self):
        if self.head is None:
            print("double linked list is empty")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=" ")
                a=a.next
    def backward_traversal(self):
        print()
        if self.head is None:
            print("singly linked list is empty")
        else:
            a=self.head
            while a.next is not None:
                a=a.next
            while a is not None:
                print(a.data,end=" ")
                a=a.prev
    def insert_at_beginning(self,data):
        print()
        nb=Node(data)
        a=self.head
        a.prev=nb
        nb.next=a
        self.head=nb
    def insert_at_end(self,data):
        print()
        nb=Node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=nb
        nb.prev=a
    def insert_at_specified_node(self,position,data):
        print()
        nib=Node(data)
        a=self.head
        for i in range(1,position-1):
            a=a.next
        nib.prev=a
        nib.next=a.next
        a.next.prev=nib
        a.next=nib
    def deletion_at_beginning(self):
        print()
        a=self.head
        self.head=a.next
        a.next=None
        self.head.prev=None
    def deletion_at_end(self):
        print()
        prev=self.head
        a=self.head.next
        while a.next is not None:
            a=a.next
            prev=prev.next
        prev.next=None
        a.prev=None
    def deletion_at_specified_node(self,position):
        print()
        prev=self.head
        a=self.head.next
        for i in range(1,position-1):
            a=a.next
            prev=prev.next
        prev.next=a.next
        a.next.prev=prev
        a.prev=None
        a.next=None

n1=Node(1)
dll=Dll()
dll.head=n1
n2=Node(10)
n2.prev=n1
n1.next=n2
n3=Node(5)
n3.prev=n2
n2.next=n3
dll.forward_traversal()
dll.backward_traversal()
dll.insert_at_beginning(4)
dll.forward_traversal()
dll.insert_at_end(3)
dll.forward_traversal()
dll.insert_at_specified_node(3,13)
dll.forward_traversal()
dll.deletion_at_beginning()
dll.forward_traversal()
dll.deletion_at_end()
dll.forward_traversal()
dll.deletion_at_specified_node(3)
dll.forward_traversal()'''

class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def is_empty(self):
        if self.head is None:
            return True
        return False
    def traversal(self):
        if self.head==None:
            print("double linked list empty")
        else:
            a=self.head
            while a is not None:
                print(a.data," ")
                a=a.next
    def insert_at_beginning(self,data):
        n=Node(data)
        a=self.head
        n.next=a
        a.prev=n
        self.head=n
    def insert_at_end(self,data):
        nb = Node(data)
        if self.is_empty():
            self.insert_at_beginning(data)
        else:
            a = self.head
            while a.next is not None:
                a = a.next
            a.next = nb
            nb.prev = a
    def insert_at_specific(self,pos,data):
        print()
        nib = Node(data)
        a = self.head
        for i in range(1, pos - 1):
            a = a.next
        nib.prev = a
        nib.next = a.next
        a.next.prev = nib
        a.next = nib
    def delete_from_beginning(self):
        if self.is_empty():
            print("LINKED LIST IS EMPTY")
        elif self.head.next is None:
            self.head=None
        else:
            a=self.head
            a.next.prev=None
            self.head=a.next
    def delete_from_end(self):
        if self.is_empty():
            print("LINKED LIST IS EMPTY")
        a=self.head
        while a.next is not None:
            a=a.next
        a.prev.next=None
    def delete_at_specific_position(self,pos):
        if self.is_empty():
            print("LINKED LIST IS EMPTY")
        elif pos==1:
            self.delete_from_beginning()
        else:
            prev = self.head
            a = self.head.next
            for i in range(1, pos - 1):
                a = a.next
                prev = prev.next
            prev.next = a.next
            a.next.prev = prev
            a.prev = None
            a.next = None



d=dll()
n1=Node(1)
d.head=n1
n2=Node(2)
n1.next=n2
n3=Node(3)
n2.prev=n1
n2.next=n3
# d.traversal()
d.insert_at_beginning(9)
print("after the insert at beginning")
d.traversal()
d.insert_at_end(10)
print("after the insert at end")
d.traversal()
d.insert_at_specific(3,56)
print("insert at specific position")
d.traversal()
d.delete_from_beginning()
print("after deletion of beginning")
d.traversal()
d.delete_from_end()
print("after deletion of end")
d.traversal()
d.delete_at_specific_position(3)
print("after deletion at specific position")
d.traversal()