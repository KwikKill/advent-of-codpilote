def calculate_score(filename):
    total_score = 0
    with open(filename, 'r') as file:
        for line in file:
            # Split the line into two parts: winning numbers and numbers
            parts = line.split('|')
            winning_numbers = set(map(int, parts[0].split(':')[1].split()))  # Get numbers after ':'
            numbers = set(map(int, parts[1].split()))

            # Calculate the score for this line
            common_numbers = winning_numbers & numbers

            if len(common_numbers) == 0:
                score = 0
            else:
                score = 2 ** (len(common_numbers) - 1)
            total_score += score

    return total_score

print(calculate_score('input.txt'))