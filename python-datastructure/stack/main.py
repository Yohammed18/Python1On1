# STACK are LIFO (last in, first out), 
# push pop peak are known functions in STACK. clear empty the stacks
# an example where a stack would be use is to program the "UNDO" function

# using a list
stack = list()

stack.append(4)
stack.append(7)
stack.append(12)
stack.append(19)

print(f"{stack}\n")
print(stack.pop())
print(stack.pop())

# Creating a wrapper stack class with the design stack methods
class Stack:
    
    def __init__(self,):
        self.stack = list()
        
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
        
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None
        
    def __str__(self):
        return str(self.stack)
        
wrapper_stack = Stack()
wrapper_stack.push(2)
wrapper_stack.push(3)
# wrapper_stack.push(10)
print("\nWrapper Stack")
print(wrapper_stack.__str__())
print(wrapper_stack.pop())
print(wrapper_stack.peek())
print(wrapper_stack.pop())   
print(wrapper_stack.pop())
print(wrapper_stack.__str__())
