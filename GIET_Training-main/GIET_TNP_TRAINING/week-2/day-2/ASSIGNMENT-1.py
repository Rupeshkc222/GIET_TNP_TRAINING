'''A teacher has given a project assignment to a class of KEEP SILENCE Students.
She wants to store the marks (out of 100) scored by each student. The marks scored are as mentioned below: 89,78,99,76,77,67,99,98,90
Write a python program to store the marks in a list and perform the following:

1. The teacher forgot to include the marks of one student. Insert 78 at index position, 8 and display the marks of all 10 students.
2. The teacher also wants to know the marks scored by students represented by index positions, 5 and 7.

Identify and display the two marks.'''


# def inset_at_pos(l,data,pos):
#     l.insert(pos,data)
#     print("the marks of all students is", l)
# l=list(map(int,input("enter the marks").split(",")))
l=[89,78,99,76,77,67,99,98,90]
l.insert(8,72)
print(l)




