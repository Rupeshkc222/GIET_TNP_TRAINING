'''
Given a linked list of characters. Write a python function to return a new string that is created by appending all the
characters given in the linked list as per the rules given below.
Rules:
Replace '*' or '/' by a single space
In case of two consecutive occurrences of '*' or '/', replace
those two occurrences by a single space and convert
the next character to upper case
Assume that
There will not be more than two consecutive occurrences of '*' or "/".
The linked list will always end with an alphabet
Sample Input
A,n,*,/,a,p,p,l,e,*,a,/,day,*,*,k,e,e,p,s,/,*,a,/,/,d,o,c,t,o,
r,*,A,w,a,y

expected output:
An apple a day Keeps a Docter Away
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Sll:
    def __init__(self):
        self.head=None
    def traversal(self):
        res=""
        if self.head is None:
            print("singly linked list is empty")
        else:
            a=self.head
            c=0
            while a is not None:
                if a.data in ['*','/']:
                    if c==0:
                        res=res+" "
                        c=1
                    if (a.next.data =='*' and a.data=='*') or (a.next.data =='/' and a.data=='/'):
                        a=a.next
                        res+=a.next.data.upper()
                        a=a.next
                    else:
                        a=a.next
                else:
                    c=0
                    res=res+a.data
                    # print(a.data,end=" ")
                a=a.next
        return res
sll=Sll()
l=['n','*','/','a','p','p','l','e','*','a','/','day','*','*','k','e','e','p','s','/','*','a','/','/','d','o','c','t','o','r','*','A','w','a','y']
# n1=Node('A')
# sll.head=n1
# n2=Node('n')
# n1.next=n2
h=Node('A')
sll.head=h
current=h
for i in l:
    current.next=Node(i)
    current=current.next
p=sll.traversal()
print(p)