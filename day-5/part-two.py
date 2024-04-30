def parse_file(filename):
    with open(filename, 'r') as file:
        content = file.read()

    sections = content.split('\n\n')  # split by empty lines
    data = {}

    for section in sections:
        lines = section.split('\n')
        title = lines[0]  # the first line is the title
        if not title.startswith('seeds:'):
            values = [list(map(int, line.split())) for line in lines[1:] if len(line.split()) == 3]  # the rest are values
            data[title] = values

    return data

def generate_seeds(filename):
    with open(filename, 'r') as file:
        content = file.read()

    sections = content.split('\n\n')  # split by empty lines
    seed_ranges = []

    for section in sections:
        lines = section.split('\n')
        title = lines[0]  # the first line is the title
        if title.startswith('seeds:'):
            seeds = list(map(int, title.split(':')[1].split()))  # split by ':' and then by spaces to get the list of seeds
            for i in range(0, len(seeds), 2):  # iterate over the seed ranges
                start, length = seeds[i], seeds[i+1]
                seed_ranges.append([start, start + length])  # append the range to the list

    return seed_ranges

data = parse_file('input.txt')
seed_ranges = generate_seeds('input.txt')
print(data)
print(seed_ranges)

def convert_range(seed_ranges, data):
    conversion_chain = ['seed-to-soil map:', 'soil-to-fertilizer map:', 'fertilizer-to-water map:', 'water-to-light map:', 'light-to-temperature map:', 'temperature-to-humidity map:', 'humidity-to-location map:']
    ranges = seed_ranges  # start with the initial range
    for map_title in conversion_chain:
        conversion_map = data[map_title]
        new_ranges = []
        for start, end in ranges:
            converted = False
            for rule in conversion_map:
                x, y, z = rule
                # continue if the range doesn't overlap with the rule
                if end <= y or y + z <= start:
                    continue
                if start < y:
                    ranges.append([start, y])  # keep the part of the range that didn't overlap with any rule
                    start = y
                if y + z < end:
                    ranges.append([y + z, end])
                    end = y + z
                new_ranges.append([x + (start - y), x + (end - y)])
                converted = True
                break
            if not converted:
                new_ranges.append([start, end])
        ranges = new_ranges
    return ranges

# Usage:
converted_ranges = convert_range(seed_ranges, data)
print(converted_ranges)
min_location = min(range[0] for range in converted_ranges)
print(min_location)