class Matrix:
    def __init__(self, rows, cols):
        """
        Initializing a matrix with given rows and columns.
        
        
        rows - Number of rows.
        cols - Number of columns.
        """
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]
    
    def insert(self, row, col, value):
        
        #Insert a value at a specific position in the matrix.
        
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Row or column index out of bounds")
        self.data[row][col] = value
    
    def delete(self, row, col):
        
        #Delete the value at a specific position in the matrix.
        
        
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Row or column index out of bounds")
        self.data[row][col] = 0  # Assuming 0 as default value
    
    def access(self, row, col):
        
        #Access the value at a specific position in the matrix.
        
        
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            raise IndexError("Row or column index out of bounds")
        return self.data[row][col]
    
    def display(self):
        #Display the matrix
        for row in self.data:
            print(row)

# Example Usage:
if __name__ == "__main__":
    matrix = Matrix(3, 3)
    matrix.insert(0, 0, 1)
    matrix.insert(1, 1, 5)
    matrix.insert(2, 2, 9)
    matrix.display()
    
    matrix.delete(1, 1)
    matrix.display()
   
    print(matrix.access(2, 2))  # Output: 9
