def calculate_power_sum(filename):
    total_power = 0
    with open(filename, 'r') as file:
        for line in file:
            _, draws = line.split(':')
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

            total_power += red_count * green_count * blue_count

    return total_power

print(calculate_power_sum('input.txt'))