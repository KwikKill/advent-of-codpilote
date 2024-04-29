def calculate_score(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Initialize the cards list with 1s
    cards = [1 for _ in range(len(lines))]

    for i, line in enumerate(lines):
        # Split the line into two parts: winning numbers and numbers
        parts = line.split('|')
        winning_numbers = set(map(int, parts[0].split(':')[1].split()))  # Get numbers after ':'
        numbers = set(map(int, parts[1].split()))

        # Calculate the score for this line
        common_numbers = winning_numbers & numbers
        score = len(common_numbers)

        # Add the current card's count to the following X cards
        for j in range(i+1, min(i+1+score, len(cards))):
            cards[j] += cards[i]

    return sum(cards)

print(calculate_score('input.txt'))