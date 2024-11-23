class Queue:
    def __init__(self):
        #Initializing an empty queue.
        self.items = []
    
    def is_empty(self):
        #Check if the queue is empty.
        return len(self.items) == 0
    
    def enqueue(self, item):
        
        #Add an item to the end of the queue.
        
        
        self.items.append(item)
    
    def dequeue(self):
        
        #Remove and return the front item of the queue.
        
       
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)
    
    def front(self):
        
        #Return the front item without removing it.
        
      
        if self.is_empty():
            raise IndexError("Front from empty queue")
        return self.items[0]
    
    def size(self):
        #Return the number of items in the queue.
        return len(self.items)
    
    def display(self):
        #Display the queue.
        print(self.items)

# Example Usage:
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()  
    print(queue.dequeue())  
    queue.display()  
    print(queue.front())  
    print(queue.size())  
