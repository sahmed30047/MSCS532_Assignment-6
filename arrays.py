class Array:
    def __init__(self, size):
        """
        Initializing an array with a fixed size.
        
        
        size (int) - The size of the array.
        """
        self.size = size
        self.data = [None] * size  # Initialize array with None
    
    def insert(self, index, value):
        
        #Insert a value at a specific index.
        
        
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.data[index] = value
    
    def delete(self, index):
       
        #Delete the value at a specific index.
        
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.data[index] = None
    
    def access(self, index):
        
       # Access the value at a specific index.
        
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.data[index]
    
    def display(self):
        #Display the contents of the array.
        print(self.data)

# Example Usage:
if __name__ == "__main__":
    array = Array(5)
    array.insert(0, 10)
    array.insert(1, 20)
    array.insert(2, 30)
    array.display()  # Output: [10, 20, 30, None, None]
    array.delete(1)
    array.display()  # Output: [10, None, 30, None, None]
    print(array.access(2))  # Output: 30
