class Node:
    def __init__(self, data):
        
        #Initialize a node with data and a pointer to the next node.
        
        
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        #Initialize an empty singly linked list.
        self.head = None
    
    def is_empty(self):
        #Check if the linked list is empty.
        return self.head is None
    
    def insert_at_beginning(self, data):
        
        #Insert a new node at the beginning of the list.
       
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_at_end(self, data):
        
        #Insert a new node at the end of the list.
      
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def delete_node(self, key):
        
       # Delete the first node with the specified data.
        
        
        current = self.head
        previous = None
        
        # If the head node holds the key
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        
        # Search for the key
        while current and current.data != key:
            previous = current
            current = current.next
        
        # If the key was not found
        if not current:
            raise ValueError(f"Node with data {key} not found.")
        
        # Unlink the node
        previous.next = current.next
        current = None
    
    def traverse(self):
        
        #Traverse the list and return a list of elements.
        
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements
    
    def display(self):
        #Display the linked list.
        elements = self.traverse()
        print(" -> ".join(map(str, elements)) if elements else "Empty List")

# Example Usage:
if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    linked_list.insert_at_end(10)
    linked_list.insert_at_beginning(5)
    linked_list.insert_at_end(15)
    linked_list.display()  
    linked_list.delete_node(10)
    linked_list.display()  
    print(linked_list.traverse())  
