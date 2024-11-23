class Stack:
    def __init__(self):
        """Initializing an empty stack."""
        self.items = []
    
    def is_empty(self):
        #Check if the stack is empty
        return len(self.items) == 0
    
    def push(self, item):
        
        #Add an item to the top of the stack.
        
        
        self.items.append(item)
    
    def pop(self):
        
        #Remove and return the top item of the stack.
        
       
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()
    
    def peek(self):
        
        #Return the top item without removing it.
        
        
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]
    
    def size(self):
        #Return the number of items in the stack.
        return len(self.items)
    
    def display(self):
        #Display the stack.
        print(self.items)

# Example Usage:
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()  
    print(stack.pop())  
    stack.display()  
    print(stack.peek())  
    print(stack.size()) 
