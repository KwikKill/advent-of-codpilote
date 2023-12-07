import re

def sum_adjacent_numbers(filename):
    with open(filename, 'r') as file:
        lines = file.read().split('\n')

    # Dynamically find symbols
    symbols = set(''.join(lines)) - set('0123456789 .\n')

    # Find numbers and their positions
    numbers = [(m.group(), (i, m.start())) for i, line in enumerate(lines) for m in re.finditer(r'\d+', line)]

    total = 0
    added_numbers = []

    # Check each number
    for number, (row, start) in numbers:
        number = int(number)
        # Check each position in the range of the number
        for pos in range(start, start + len(str(number))):
            # Check each adjacent position
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    adj_row, adj_col = row + dr, pos + dc
                    # If the adjacent position is within the content and contains a symbol
                    if 0 <= adj_row < len(lines) and 0 <= adj_col < len(lines[adj_row]) and lines[adj_row][adj_col] in symbols:
                        # If the number hasn't been added yet, add it to the total
                        if (number, row, start) not in added_numbers:
                            total += number
                            added_numbers.append((number, row, start))
                        break
    return total

print(sum_adjacent_numbers('input.txt'))    