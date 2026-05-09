def calculate_total_value(solution, items):
    """
    Calculate the total value of a list of item names.

    Args:
        solution: list of item name strings
        items: list of (name, weight, value) tuples

    Returns:
        int: sum of values for every name in solution
    """
    total = 0
    for name in solution:
        for item_name, weight, value in items:
            if item_name == name:
                total += value
                break
    return total


def knapsack(items, capacity):
    """
    Solve the knapsack problem using dynamic programming.

    Args:
        items: List of tuples (name, weight, value)
        capacity: Maximum weight capacity of knapsack

    Returns:
        2D grid showing optimal solutions for each subproblem
    """
    n = len(items)
    # Create a 2D grid to store solutions
    # grid[i][w] will store the best items for first i items with capacity w
    grid = [[[] for _ in range(capacity + 1)] for _ in range(n + 1)]

    # TODO 2-5: Fill in the dynamic programming logic
    # Hint: For each item and each capacity, decide whether to include the item or not
    for i in range(1, n + 1):
        item_name, weight, value = items[i - 1]
        for w in range(1, capacity + 1):
            # TODO 2: Check if current item's weight exceeds current capacity
            if weight > w:
                # Can't include this item, copy from above (slice-copy!)
                grid[i][w] = grid[i - 1][w][:]
            else:
                # TODO 3: Build the two candidate solutions
                include_solution = grid[i - 1][w - weight][:] + [item_name]
                exclude_solution = grid[i - 1][w][:]

                # TODO 4: Convert each candidate to a dollar value
                include_value = calculate_total_value(include_solution, items)
                exclude_value = calculate_total_value(exclude_solution, items)

                # TODO 5: Store the winner
                if include_value > exclude_value:
                    grid[i][w] = include_solution
                else:
                    grid[i][w] = exclude_solution

    return grid


def display_grid(grid, items):
    """
    Display the DP grid in a readable format.

    Args:
        grid: 2D grid from knapsack function
        items: List of tuples (name, weight, value)
    """
    n = len(items)
    capacity = len(grid[0]) - 1
    cell_width = 12

    # TODO 6: Build the header row
    header = " " * cell_width
    for i in range(1, capacity + 1):
        header += "{:>{width}}".format(str(i), width=cell_width)
    print(header)

    # TODO 7-9: Print each data row
    for i in range(1, n + 1):
        # TODO 7: Start with item name left-aligned in 12 chars
        row = "{:<{width}}".format(items[i - 1][0], width=cell_width)
        for w in range(1, capacity + 1):
            cell = grid[i][w]
            if cell:
                # TODO 8: Format as $VALUE(LETTERS)
                val = calculate_total_value(cell, items)
                letters = "".join(name[0] for name in cell)
                cell_str = "${val}({letters})".format(val=val, letters=letters)
                row += "{:>{width}}".format(cell_str, width=cell_width)
            else:
                # TODO 9: Empty cell
                row += " " * cell_width
        print(row)


if __name__ == "__main__":
    items = [
        ("GUITAR", 1, 1500),
        ("STEREO", 4, 3000),
        ("LAPTOP", 3, 2000),
        ("iPHONE", 1, 2000),
        ("BOOK", 2, 100),
        ("GOLD BAR", 1, 30000),
    ]
    capacity = 6

    # TODO 10: Replace None with a call to knapsack
    grid = knapsack(items, capacity)

    # TODO 11: Uncomment the display_grid line
    display_grid(grid, items)
