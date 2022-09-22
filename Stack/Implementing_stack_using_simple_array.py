class Stack:
    def __init__(self,limit=10):
        self.stk = []
        self.limit = limit

    # Function to add item in the Stack
    def push(self,item):
        if len(self.stk) >= self.limit:
            print("Stack Overflow")
        else:
            self.stk.append(item)

        print("Stack after push --> ",self.stk)

    # Function to remove an item from the Stack
    def pop(self):
        if len(self.stk) <=0:
            print("Stack Underflow")
            return 0
        else:
            return self.stk.pop()

    # Function to check if the Stack is empty
    def isEmpty(self):
        return len(self.stk) <= 0

    # Function to get the top item from the Stack without removing
    def peek(self):
        if len(self.stk)<=0:
            print('Stack Underflow')
            return 0
        else:
            return self.stk[-1]

    # Function to return the size of stack
    def size(self):
        return len(self.stk)


#Driver Code
if __name__=="__main__":
    our_stack = Stack(5)
    our_stack.push(5)
    our_stack.push(7)
    our_stack.push(3)
    print(our_stack.pop())
    print(our_stack.size())
    print(our_stack.peek())
    our_stack.push(10)
    print(our_stack)

