import random

def randomized_select(A, k):
    
    #Select the k-th smallest element in A using the Randomized Quickselect algorithm.
    
    
    #Return - The k-th smallest element in A.
    
    if not 1 <= k <= len(A):
        raise ValueError("k is out of bounds")
    
    def select(lst, k):
        if len(lst) == 1:
            return lst[0]
        
        # Randomly select a pivot
        pivot = random.choice(lst)
        
        lows = [el for el in lst if el < pivot]
        highs = [el for el in lst if el > pivot]
        pivots = [el for el in lst if el == pivot]
        
        if k <= len(lows):
            return select(lows, k)
        elif k > len(lows) + len(pivots):
            return select(highs, k - len(lows) - len(pivots))
        else:
            return pivots[0]
    
    return select(A, k)

# Example Usage:
if __name__ == "__main__":
    array = [22, 13, 2, 7, 4, 19, 23]
    k = 3
    print(f"The {k}rd smallest element is {randomized_select(array, k)}")
