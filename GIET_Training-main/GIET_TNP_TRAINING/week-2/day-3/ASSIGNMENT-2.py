'''Given a stack of integers, write a python program that updates the input stack such that all occurrences of the
smallest values are at the bottom of the stack, while the order of the other elements remains the same.

For example:

Input stack (top-bottom) : 5 66 5 8 7
Output: 66 8 7 5 5 '''



def up_date(n):
    m=min(n)
    c=n.count(m)
    for i in range(c):
        n.remove(m)
        n.append(m)
    return n

n=[5,66,5,8,7]
r=up_date(n)
print(r)