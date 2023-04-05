#Traversal in linked list
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
    def insert_at_beginning(self,data):
        print()
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def insert_at_end(self,data):
        print()
        ne=Node(data)
        a=self.head
        while a.next is not None:
            a=a.next
        a.next=ne
    def insert_at_specified_node(self,position,data):
        print()
        nib=Node(data)
        a=self.head
        for i in range(1,position-1):
            a=a.next
        nib.next=a.next
        a.next=nib
    def deletion_at_beginning(self):
        print()
        a=self.head
        self.head=a.next
        a.next=None
    def deletion_at_end(self):
        print()
        prev=self.head
        a=self.head.next
        while a.next is not None:
            a=a.next
            prev=prev.next
        prev.next=None
    def deletion_at_specified_node(self,position):
        print()
        prev=self.head
        a=self.head.next
        for i in range(1,position-1):
            a=a.next
            prev=prev.next
        prev.next=a.next
        a.next=None


n1=Node(1)
sll=Sll()
sll.head=n1
n2=Node(10)
n1.next=n2
sll.traversal()
sll.insert_at_beginning(6)
sll.traversal()
sll.insert_at_end(4)
sll.traversal()
sll.insert_at_specified_node(3,7)
sll.traversal()
sll.deletion_at_beginning()
sll.traversal()
sll.deletion_at_end()
sll.traversal()
sll.deletion_at_specified_node(3)
sll.traversal()


#Traversal in Doubly linked list
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
            print("singly linked list is empty")
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


#binary tree implimentation
  #INORDER-->left root right
  #PREORDER-->root left right
  #POSTORDER-->left right root

'''class Node:
    def __init__(self,key):
        self.left =None
        self.right = None
        self.val=key
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val,end=" ")
        if self.right:
            self.right.inorder()
    def preorder(self):
        print(self.val,end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.val,end=" ")    
        
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left = Node(4)

print("In order traversal :", end="")
root.inorder()
print("Pre order traversal :", end="")
root.preorder()
print("Post order traversal :", end="")
root.postorder()'''

#D = {'a':0,'b':1,'c':2}
#print(D.values())


'''def converMarks(marks):
    
    for a,y in marks.items():
        for x in y:
            if marks[x]>= 91 and marks[x]<=100:
                marks[x]='A'
            elif marks[x]>= 81 and marks[x]<=90:
                marks[x]='A'
            elif marks[x]>= 71 and marks[x]<=80:
                marks[x]='A'
            elif marks[x]>= 61 and marks[x]<=70:
                marks[x]='A'
            elif marks[x]>= 51 and marks[x]<=60:
                marks[x]='E+'
            elif marks[x]>= 41 and marks[x]<=50:
                marks[x]='E'
            elif marks[x]>= 0 and marks[x]<=40:
                marks[x]='F'    
    return (marks)
        
print(converMarks({'Lakshman': {'Maths': 90, 'English': 75, 'Social Science': 10}}))'''

'''name = input().split()

d = {}
for i in name:
    d[i] = {}
    subjects = input().split()
    marks = input().split()
    for j in range(len(subjects)):
        d[i][subjects[j]] = int(marks[j])

print(converMarks(d))'''








'''def maxSum(arr,n):
    # code here
    if len(arr)==1:
        return arr[0]
    f=[sorted(arr)]
    l=f[::-1]
    narr=[]
    print(f,l)
    for i in range(len(arr)):
        if i%2==0:
            narr.append(f[0])
            print("ok")
            f.pop(f[0])
            l.remove(l[-1])
        else:
            narr.append(l[0])
            l.remove(l[0])
            f.remove(f[-1])
    s=0
    for i in range(len(narr)-1):
        s=s+abs(narr[i]-narr[i+1])
    return s+abs(narr[-1]-narr[0])'''
    
    


#{ 
#Driver Code Starts
#Initial Template for Python 3



#t=int(input())
#for _ in range(0,t):
    #n=int(input())
    # x=list(map(int,input().split()))
    # n=x[0]
    # k=x[1]
    #arr = list(map(int,input().split()))
'''ans=maxSum([4,2,1,8],4)
print(ans)'''


'''arr=[93,85,-59,45,-89,-41,-4,-98,79,-12]
p=[]
n=[]
for i in arr:
    if i>=0 :
        p.append(i)
    else:
        n.append(i)
print(p,n)
if len(p)==0 or len(n)==0:
    print(arr)
a=0
b=0
f=0
for i in range(len(arr)):
    if f==0 and a<len(p):
        arr[i]=p[a]
        print(arr[i])
        a+=1
        f=1
    elif f==1 and b<len(n):
        arr[i]=n[b]
        print(arr[i])
        b+=1
        f=0
    elif a==len(p):
        print(a,b,i)   #check 
        arr[i:]=n[b:]
        break
    elif b==len(n):
        print(a,b,i) #check
        arr[i:]=p[a:]
        break
   

print( arr)'''




'''import math
A=[-8,2,3,-6,10]
N=len(A)
k=2
res=[]
print(math.floor(N-(N//k)))
for i in range(0,N-(N//k)):
    a=A[i:i+k]
    print(a)
    c=0
    for j in a:
        if j <0:
            c+=1
            break
    if c==1:
        res.append(j)
        print("negative nikla")
    else:
        print("nahi nikla")
        res.append(c)
    print(res)
print( res)'''





'''A=[-1,-15]
N=len(A)
k=1
res=[]
b=N-k
neg=[]'''
'''for i in range(0,b+1):
    a=A[i:i+k]
    print(a)
    if i==0:
        for j in a:
            if j<0:
                neg.append(j)
                print(neg,"after append")
    if len(neg) !=0:
        res.append(neg[0])
        print(res,"res me dala")
        if neg[0] == A[i]:
            neg.pop(0)
            print(neg,"after pop")
    else:
        res.append(0)
print(res)'''
'''n=0
c=0
for i in range(0,b+1):
    for j in range(n,i+k):
        if A[j]<0 and A[j] not in neg:
            neg.append(A[j])
            print("neg me append hua",neg)
    if len(neg)!=0:
        res.append(neg[0])
        print("res me append hua",res)
    else:
        res.append(0)
        print("res me 0 append hua")
    if len(neg)!=0 and neg[0] == A[i]:
        neg.pop(0)
        print("neg me pop hua",neg)
    n=j+1
print(res)'''




