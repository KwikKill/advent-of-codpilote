import re

def process_file(filename):
    with open(filename, 'r') as file:
        grid = [line.strip() for line in file]

    total = 0

    # Iterate over each line and character in the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # If the character is "*"
            if grid[i][j] == '*':
                # Check the four cells in diagonal plus the two on the side
                cells = [(i + di, j + dj) for di, dj in [(-1, -1), (-1, 1), (1, -1), (1, 1), (0, -1), (0, 1)] if 0 <= i + di < len(grid) and 0 <= j + dj < len(grid[i + di]) and grid[i + di][j + dj].isdigit()]
                # If at least two of them are digits
                if len(cells) >= 2:
                    # Use a regexp to find every number in the 3 lines above, same and below the "*" char, with only 7 chars long (center on "*")
                    numbers = []
                    for x in range(i - 1, i + 2):
                        if 0 <= x < len(grid):
                            dj1 = j-1
                            while dj1 >= 0 and dj1>= j-3:
                                if not grid[x][dj1].isdigit():
                                    break
                                dj1 -= 1
                            dj2 = j+1
                            while dj2 < len(grid[x]) and dj2 <= j+3:
                                if not grid[x][dj2].isdigit():
                                    break
                                dj2 += 1
                            line = grid[x][max(0, dj1):min(len(grid[x]), dj2)]
                            numbers.extend([int(num) for num in re.findall(r'\d+', line)])
                    # Multiply these numbers and add them to the total
                    if len(numbers) == 2:
                        total += numbers[0] * numbers[1]

    return total

print(process_file('input.txt'))