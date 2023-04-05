class Stack:
    def __init__(self,max_size):
        self.max_size=max_size
        self.element=[None]*self.max_size
        self.top=-1
    def is_full(self):
        if(self.top==self.max_size-1):
            return True
        return False
    def is_empty(self):
        if (self.top==-1):
            return True
        return False
    def push(self,data):
        if (self.is_full()):
            print("the stack is full")
        else:
            self.top+=1
            self.element[self.top]=data
    def pop(self):
        if self.is_empty():
            print("the stack is empty")
        else:
            data=self.element[self.top]
            self.top-=1
            return data
    def display(self):
        if (self.is_empty()):
            print("Stack is empty")
        else:
            index=self.top
            while index >=0:
                print(self.element[index])
                index-=1
    def get_max_size(self):
        return self.max_size

ball_stack=Stack(4)
print ("Is it empty",ball_stack.is_empty())
ball_stack.push(5)
print ("Is it empty",ball_stack.is_empty())
ball_stack.push(6)
ball_stack.push(7)
ball_stack.push(8)
ball_stack.display()
print ("size of the stack", ball_stack.get_max_size())
print ("the elemnt deleted", ball_stack.pop())
print ("after deleting the element")
ball_stack.display()
print ("size of the stack", ball_stack.get_max_size())


