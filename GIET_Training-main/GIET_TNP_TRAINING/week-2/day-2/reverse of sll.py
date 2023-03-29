class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Sll:
    def __init__(self):
        self.head=None
    def traversal(self):
        if self.head is None:
            print("singly linked list is empty")
        else:
            a=self.head
            while a is not None:
                print(a.data,end=" ")
                a=a.next
    def reverse(self):
        print()
        prev = None
        curr = self.head
        while (curr is not None):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

n1=Node(1)
sll=Sll()
sll.head=n1
n2=Node(10)
n1.next=n2
n3=Node(11)
n2.next=n3
print("value before reverse")
sll.traversal()
sll.reverse()
print("value after the reverse")
sll.traversal()