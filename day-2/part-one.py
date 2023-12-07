def find_game(filename):
    total_game_id = 0
    with open(filename, 'r') as file:
        for line in file:
            game_id, draws = line.split(':')
            game_id = int(game_id.split()[1])  # Extract the game number and convert to int
            draws = draws.split(';')

            red_count = green_count = blue_count = 0

            for draw in draws:
                cubes = draw.split(',')
                for cube in cubes:
                    count, color = cube.strip().split()
                    count = int(count)

                    if color == 'red':
                        red_count = max(red_count, count)
                    elif color == 'green':
                        green_count = max(green_count, count)
                    elif color == 'blue':
                        blue_count = max(blue_count, count)

            if red_count <= 12 and green_count <= 13 and blue_count <= 14:
                total_game_id += game_id

    return total_game_id

print(find_game('input.txt'))