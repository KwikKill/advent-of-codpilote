def sum_calibration_values(filename):
    total = 0
    word_to_digit = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    with open(filename, 'r') as file:
        for line in file:
            digits = []
            i = 0
            while i < len(line):
                char = line[i]
                if char.isdigit():
                    digits.append(char)
                elif char.isalpha():
                    for j in range(i+1, len(line) + 1):
                        word = line[i:j]
                        if word in word_to_digit:
                            digits.append(word_to_digit[word])
                            break
                i += 1
            print(line, digits)
            if digits:
                total += int(digits[0] + digits[-1])
    return total

print(sum_calibration_values('input.txt'))