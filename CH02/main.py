"""
Lab 2: Main Program
Demonstrates selection sort and array vs linked list.
"""
import json
import time
from sort import selection_sort, python_builtin_sort
from linked_list import LinkedList


def load_cities(filename: str) -> list:
    """Load cities from JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)


def main():
    # TODO: Load city data from 'data/cities.json'
    # cities = load_cities('data/cities.json')
    # print(f"Loaded {len(cities)} cities\n")
    
    # =========================================
    # PART 1: Selection Sort
    # =========================================
    # TODO: Implement Part 1
    # 1. Print header
    # 2. Sort cities by population (ascending) using selection_sort
    # 3. Print top 5 smallest cities
    # 4. Sort cities by population (descending) using selection_sort with reverse=True
    # 5. Print top 5 largest cities
    # 6. Compare with python_builtin_sort
    
    pass  # Remove this and add your code
    
    # =========================================
    # PART 2: Array vs Linked List
    # =========================================
    # TODO: Implement Part 2
    # 1. Demonstrate array (Python list) operations
    #    - Access by index - O(1)
    #    - Insert at beginning - O(n)
    # 2. Demonstrate linked list operations
    #    - Create LinkedList and insert cities
    #    - Insert at head - O(1)
    #    - Search for a city - O(n)
    
    pass  # Remove this and add your code
    
    # =========================================
    # PART 3: Big O Comparison
    # =========================================
    # TODO: Print Big O summary
    # Selection Sort: O(n²)
    # Python's Timsort: O(n log n)
    # Array vs Linked List comparison table
    
    pass  # Remove this and add your code


if __name__ == "__main__":
    main()
