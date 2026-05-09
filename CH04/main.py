def quicksort(array):
    # Base case
    if len(array) < 2:
        return array
    
    # Choose pivot
    pivot = array[0]
    
    # Partition
    less = [x for x in array[1:] if x <= pivot]
    greater = [x for x in array[1:] if x > pivot]
    
    # Recurse and combine
    return quicksort(less) + [pivot] + quicksort(greater)


# Test cases (these should print when you click Run)
print(quicksort([10, 5, 2, 3]))
print(quicksort([10, 33, 15]))
print(quicksort([5, 4, 3, 2, 1]))
print(quicksort([1]))
print(quicksort([]))
print(quicksort([8, 7, 6, 5, 4, 3, 2, 1]))
