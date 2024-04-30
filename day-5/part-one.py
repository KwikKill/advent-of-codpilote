def parse_file(filename):
    with open(filename, 'r') as file:
        content = file.read()

    sections = content.split('\n\n')  # split by empty lines
    data = {}
    seeds = []

    for section in sections:
        lines = section.split('\n')
        title = lines[0]  # the first line is the title
        if title.startswith('seeds:'):
            seeds = list(map(int, title.split(':')[1].split()))  # split by ':' and then by spaces to get the list of seeds
        else:
            values = [list(map(int, line.split())) for line in lines[1:]]  # the rest are values
            data[title] = values

    return seeds, data

seeds, data = parse_file('input.txt')
print(seeds)
print(data)

def convert_seed(seed, data):
    conversion_chain = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:', 'water-to-light map:', 'light-to-temperature map:', 'temperature-to-humidity map:', 'humidity-to-location map:']
    for map_title in conversion_chain:
        conversion_map = data[map_title]
        for rule in conversion_map:
            x, y, z = rule
            if y <= seed < y + z:
                seed = x + (seed - y)
                break
    return seed

# Usage:
converted_seeds = [convert_seed(seed, data) for seed in seeds]
print(converted_seeds)
min_location = min(converted_seeds)
print(min_location)