def deterministic_select(A, k):
    """
    Select the k smallest element in A using the Median of Medians algorithm.
    
   
    A (list):The list of elements.
    k (int): The order of the smallest element to find (1-based index).
    
    Returns    The k-th smallest element in A.
    """
    if not 1 <= k <= len(A):
        raise ValueError("k is out of bounds")

    def median_of_medians(lst):
        """Find the median of medians."""
        # Divide lst into sublists of at most five elements
        sublists = [lst[i:i + 5] for i in range(0, len(lst), 5)]
        # Sort each sublist and find its median
        medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
        # If there's only one median, return it
        if len(medians) == 1:
            return medians[0]
        # Otherwise, recursively find the median of medians
        return median_of_medians(medians)

    def select(lst, k):
        """Recursive selection function."""
        if len(lst) == 1:
            return lst[0]
        
        pivot = median_of_medians(lst)
        
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
    array = [13, 3, 6, 7, 4, 17, 26]
    k = 3
    print(f"The {k}rd smallest element is {deterministic_select(array, k)}")
